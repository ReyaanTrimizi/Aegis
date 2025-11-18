"""
AEGIS Server Logic
Reactive handlers and output rendering
"""

from shiny import ui, render, reactive
from shinywidgets import render_plotly
import pandas as pd
import json
from data import BASE_DATA
from utils import filter_data, create_chart, format_currency, parse_simple_text, validate_chart_config
from config import FIELD_DISPLAY_NAMES, NUMERIC_FIELDS, CATEGORICAL_FIELDS, COLORS


def server(input, output, session):
    
    # Reactive values
    filtered_data = reactive.Value(BASE_DATA.copy())
    
    chart_config = reactive.Value({
        'type': 'Bar Chart', 'x': 'department', 'y': 'cost_m',
        'color': 'category', 'trendline': False
    })
    
    advanced_chart_config = reactive.Value({
        'type': 'Bar Chart', 'x': 'department', 'y': 'cost_m',
        'color': 'category', 'trendline': False
    })
    
    # Dynamic field options based on chart type
    @reactive.Effect
    def _():
        chart_type = input.chart_type()
        
        if chart_type == "Bar Chart":
            x_options = {field: FIELD_DISPLAY_NAMES[field] for field in CATEGORICAL_FIELDS + NUMERIC_FIELDS}
            y_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
        elif chart_type == "Scatter Plot":
            x_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
            y_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
        elif chart_type == "Box Plot":
            x_options = {field: FIELD_DISPLAY_NAMES[field] for field in CATEGORICAL_FIELDS}
            y_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
        elif chart_type == "Histogram":
            x_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
            y_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
        else:
            x_options = {field: FIELD_DISPLAY_NAMES[field] for field in CATEGORICAL_FIELDS + NUMERIC_FIELDS}
            y_options = {field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS}
        
        ui.update_select("x_axis", choices=x_options)
        ui.update_select("y_axis", choices=y_options)
    
    # Preset button handlers
    @reactive.Effect
    @reactive.event(input.preset_full)
    def _():
        ui.update_checkbox_group("filter_department", selected=["Army", "Navy", "Air Force", "Marines"])
        ui.update_checkbox_group("filter_category", selected=["Vehicles", "Aircraft", "Communications", "Weapons"])
        ui.update_checkbox_group("filter_priority", selected=["Critical", "High", "Medium"])
        ui.update_slider("max_budget", value=400)
        ui.update_slider("min_roi", value=1.0)
    
    @reactive.Effect
    @reactive.event(input.preset_budget)
    def _():
        ui.update_checkbox_group("filter_department", selected=["Army", "Navy", "Air Force", "Marines"])
        ui.update_checkbox_group("filter_category", selected=["Vehicles", "Aircraft", "Communications", "Weapons"])
        ui.update_checkbox_group("filter_priority", selected=["Critical", "High"])
        ui.update_slider("max_budget", value=200)
        ui.update_slider("min_roi", value=1.3)
    
    @reactive.Effect
    @reactive.event(input.preset_value)
    def _():
        ui.update_checkbox_group("filter_department", selected=["Army", "Navy", "Air Force", "Marines"])
        ui.update_checkbox_group("filter_category", selected=["Vehicles", "Aircraft", "Communications", "Weapons"])
        ui.update_checkbox_group("filter_priority", selected=["Critical", "High", "Medium"])
        ui.update_slider("max_budget", value=300)
        ui.update_slider("min_roi", value=1.4)
    
    # Filter data reactively
    @reactive.Effect
    def _():
        df = filter_data(
            BASE_DATA,
            list(input.filter_department()),
            list(input.filter_category()),
            list(input.filter_priority()),
            input.max_budget(),
            input.min_roi()
        )
        filtered_data.set(df)
    
    # Chart configuration
    @reactive.Effect
    @reactive.event(input.apply_chart)
    def _():
        chart_config.set({
            'type': input.chart_type(),
            'x': input.x_axis(),
            'y': input.y_axis(),
            'color': input.color_by(),
            'trendline': input.show_trendline()
        })
    
    # Summary cards
    @output
    @render.ui
    def card_count():
        df = filtered_data.get()
        return ui.div(
            ui.div("Items Count", class_="metric-label"),
            ui.div(str(len(df)), class_="metric-value"),
        )
    
    @output
    @render.ui
    def card_cost():
        df = filtered_data.get()
        total = df['cost_m'].sum() if not df.empty else 0
        return ui.div(
            ui.div("Total Cost", class_="metric-label"),
            ui.div(format_currency(total), class_="metric-value"),
        )
    
    @output
    @render.ui
    def card_roi():
        df = filtered_data.get()
        avg = df['roi'].mean() if not df.empty else 0
        return ui.div(
            ui.div("Average ROI", class_="metric-label"),
            ui.div(f"{avg:.2f}x", class_="metric-value"),
        )
    
    @output
    @render.ui
    def card_value():
        df = filtered_data.get()
        avg = df['value_score'].mean() if not df.empty else 0
        return ui.div(
            ui.div("Avg Value Score", class_="metric-label"),
            ui.div(f"{avg:.3f}", class_="metric-value"),
        )
    
    # Main chart
    @render_plotly
    def main_chart():
        df = filtered_data.get()
        config = chart_config.get()
        return create_chart(df, config['type'], config['x'], config['y'], config['color'], config['trendline'])
    
    # Data table
    @render.data_frame
    def data_table():
        df = filtered_data.get()
        
        if df.empty:
            return pd.DataFrame({"Message": ["No items match current filters"]})
        
        display_df = df[[
            'upgrade_id', 'upgrade_name', 'department', 'category',
            'cost_m', 'roi', 'maintenance_pct', 'age_years',
            'lifespan_years', 'value_score'
        ]].copy()
        
        display_df.columns = ['ID', 'Name', 'Dept', 'Category', 'Cost', 'ROI', 'Maint', 'Age', 'Lifespan', 'Value']
        display_df['Cost'] = display_df['Cost'].apply(lambda x: f"${x:.0f}M")
        display_df['ROI'] = display_df['ROI'].apply(lambda x: f"{x:.2f}x")
        display_df['Maint'] = display_df['Maint'].apply(lambda x: f"{x*100:.0f}%")
        display_df['Value'] = display_df['Value'].apply(lambda x: f"{x:.3f}")
        display_df = display_df.sort_values('Value', ascending=False)
        
        return display_df
    
    # Custom chart configuration
    @reactive.Effect
    @reactive.event(input.generate_chart)
    def _():
        query_text = input.query_input()
        if not query_text or not query_text.strip():
            return
        
        try:
            config = json.loads(query_text)
            errors = validate_chart_config(config)
            if errors:
                return
            
            advanced_chart_config.set({
                'type': config.get('chart_type', 'Bar Chart'),
                'x': config.get('x_axis', 'department'),
                'y': config.get('y_axis', 'cost_m'),
                'color': config.get('color_by', 'None'),
                'trendline': config.get('show_trendline', False)
            })
        except json.JSONDecodeError:
            config = parse_simple_text(query_text)
            advanced_chart_config.set({
                'type': config['chart_type'],
                'x': config['x_axis'],
                'y': config['y_axis'],
                'color': config['color_by'],
                'trendline': config['show_trendline']
            })
    
    @output
    @render.ui
    def query_status():
        query_text = input.query_input()
        if not query_text or not query_text.strip():
            return ui.div()
        
        try:
            config = json.loads(query_text)
            errors = validate_chart_config(config)
            
            if errors:
                error_list = ui.tags.ul(*[ui.tags.li(error, style=f"color: {COLORS['text']};") for error in errors])
                return ui.div(
                    ui.tags.div("Configuration Error:", style=f"color: {COLORS['accent_red']}; font-weight: 600; margin-top: 1rem; margin-bottom: 0.5rem;"),
                    error_list
                )
            else:
                x_display = FIELD_DISPLAY_NAMES.get(config.get('x_axis'), config.get('x_axis', ''))
                y_display = FIELD_DISPLAY_NAMES.get(config.get('y_axis'), config.get('y_axis', ''))
                return ui.div(
                    ui.tags.span(f"{config.get('chart_type', 'Bar Chart')}: ", style=f"color: {COLORS['accent_green']}; font-weight: 600; margin-top: 1rem;"),
                    ui.tags.span(f"{x_display} vs {y_display}", style=f"color: {COLORS['text']};"),
                    style="margin-top: 1rem; display: block;"
                )
        except json.JSONDecodeError:
            return ui.div(
                ui.tags.div("Invalid JSON format. Please check your syntax (commas, quotes, braces).", 
                           style=f"color: {COLORS['accent_orange']}; font-weight: 600; margin-top: 1rem;")
            )
    
    # Advanced chart
    @render_plotly
    def advanced_chart():
        df = filtered_data.get()
        config = advanced_chart_config.get()
        return create_chart(df, config['type'], config['x'], config['y'], config['color'], config['trendline'])

