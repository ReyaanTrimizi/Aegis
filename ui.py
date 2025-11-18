"""
AEGIS UI Definition
Complete user interface layout
"""

from shiny import ui
from shinywidgets import output_widget
from config import (
    COLORS, FIELD_DISPLAY_NAMES, COLOR_DISPLAY_NAMES,
    CATEGORICAL_FIELDS, NUMERIC_FIELDS, COLOR_OPTIONS
)
from styles import get_custom_css


app_ui = ui.page_fluid(
    ui.tags.head(ui.tags.style(get_custom_css())),
    
    # Header
    ui.div(
        ui.div(
            ui.h1("AEGIS", class_="header-title"),
            ui.div(
                ui.p("Defense Equipment Portfolio Analyzer", class_="header-subtitle"),
                ui.p("Budget Optimization & Value Assessment", class_="header-description"),
                class_="header-content"
            ),
            class_="header-container"
        ),
        class_="navbar"
    ),
    
    # Main content with tabs
    ui.navset_pill(
        # Dashboard tab
        ui.nav_panel(
            "Dashboard",
            ui.layout_sidebar(
                # Sidebar
                ui.sidebar(
                    ui.div(
                        ui.div("DEPARTMENT", class_="section-title"),
                        ui.input_checkbox_group(
                            "filter_department", None,
                            ["Army", "Navy", "Air Force", "Marines"],
                            selected=["Army", "Navy", "Air Force", "Marines"]
                        ),
                        
                        ui.div("CATEGORY", class_="section-title"),
                        ui.input_checkbox_group(
                            "filter_category", None,
                            {"Vehicles": "Vehicles", "Aircraft": "Aircraft", "Communications": "Comms", "Weapons": "Weapons"},
                            selected=["Vehicles", "Aircraft", "Communications", "Weapons"]
                        ),
                        
                        ui.div("PRIORITY", class_="section-title"),
                        ui.input_checkbox_group(
                            "filter_priority", None,
                            ["Critical", "High", "Medium"],
                            selected=["Critical", "High", "Medium"]
                        ),
                        
                        ui.div("MAX BUDGET", class_="section-title"),
                        ui.input_slider("max_budget", None, min=100, max=400, value=300, step=20, post="M"),
                        
                        ui.div("MIN ROI", class_="section-title"),
                        ui.input_slider("min_roi", None, min=1.0, max=1.8, value=1.2, step=0.1, post="x"),
                        
                        ui.div("PRESETS", class_="section-title"),
                        ui.input_action_button("preset_full", "Full Portfolio", class_="btn-primary"),
                        ui.input_action_button("preset_budget", "Budget Constrained", class_="btn-primary"),
                        ui.input_action_button("preset_value", "High Value Only", class_="btn-primary"),
                        
                        class_="sidebar"
                    ),
                    width=300,
                    bg=COLORS['panel']
                ),
                
                # Main content area
                ui.div(
                    # Summary cards
                    ui.row(
                        ui.column(3, ui.div(ui.output_ui("card_count"), class_="metric-card")),
                        ui.column(3, ui.div(ui.output_ui("card_cost"), class_="metric-card")),
                        ui.column(3, ui.div(ui.output_ui("card_roi"), class_="metric-card")),
                        ui.column(3, ui.div(ui.output_ui("card_value"), class_="metric-card")),
                    ),
                    
                    # Chart area
                    ui.div(
                        ui.h4("Interactive Chart"),
                        ui.div(
                            ui.row(
                                ui.column(2, ui.input_select("chart_type", "Chart Type", {
                                    "Bar Chart": "Bar Chart",
                                    "Scatter Plot": "Scatter Plot",
                                    "Box Plot": "Box Plot",
                                    "Histogram": "Histogram"
                                }, selected="Bar Chart")),
                                ui.column(3, ui.input_select("x_axis", "X-Axis Field", {
                                    field: FIELD_DISPLAY_NAMES[field] for field in CATEGORICAL_FIELDS + NUMERIC_FIELDS
                                }, selected="department")),
                                ui.column(3, ui.input_select("y_axis", "Y-Axis Field", {
                                    field: FIELD_DISPLAY_NAMES[field] for field in NUMERIC_FIELDS
                                }, selected="cost_m")),
                                ui.column(2, ui.input_select("color_by", "Color By", {
                                    opt: COLOR_DISPLAY_NAMES[opt] for opt in COLOR_OPTIONS
                                }, selected="category")),
                                ui.column(2, ui.div(
                                    ui.input_checkbox("show_trendline", "Show Trendline", value=False),
                                    ui.tags.small("(Scatter plots only)", style=f"color: {COLORS['text_secondary']}; font-size: 0.7rem;"),
                                    style="padding-top: 1.75rem;"
                                )),
                                ui.column(2, ui.input_action_button("apply_chart", "Apply Changes", class_="btn-primary"), style="padding-top: 1.5rem;")
                            ),
                            class_="chart-controls"
                        ),
                        output_widget("main_chart"),
                        class_="card"
                    ),
                    
                    # Data table
                    ui.div(
                        ui.h4("Equipment Portfolio Data"),
                        ui.output_data_frame("data_table"),
                        class_="card"
                    ),
                    
                    style="padding: 1.5rem;"
                )
            )
        ),
        
        # Custom Charts tab
        ui.nav_panel(
            "Custom Charts",
            ui.div(
                ui.div(
                    ui.h3("Custom Chart Builder", style="margin-bottom: 1rem; color: #f5f7fa;"),
                    ui.p("Create custom charts by editing the JSON configuration below. Change any values and click Generate.", 
                         style=f"color: {COLORS['text']}; margin-bottom: 0.5rem; line-height: 1.6;"),
                    ui.tags.div(
                        ui.tags.strong("Quick Guide: ", style=f"color: {COLORS['accent_blue']};"),
                        ui.tags.span("chart_type: Bar Chart, Scatter Plot, Box Plot, Histogram  |  ", style=f"color: {COLORS['text']};"),
                        ui.tags.span("x_axis/y_axis: cost_m, roi, value_score, department, category  |  ", style=f"color: {COLORS['text']};"),
                        ui.tags.span("color_by: department, category, priority", style=f"color: {COLORS['text']};"),
                        style="font-size: 0.85rem; margin-top: 0.5rem;"
                    ),
                    class_="card"
                ),
                
                ui.div(
                    ui.input_text_area("query_input", "Chart Configuration", value='''{
  "chart_type": "Scatter Plot",
  "x_axis": "cost_m",
  "y_axis": "roi",
  "color_by": "department",
  "show_trendline": false
}''', rows=10, width="100%"),
                    ui.input_action_button("generate_chart", "Generate Chart", class_="btn-primary", style="margin-top: 1rem; width: 200px;"),
                    ui.output_ui("query_status"),
                    class_="card",
                    style="margin-top: 1.5rem;"
                ),
                
                ui.div(
                    ui.h4("Generated Chart", style=f"color: {COLORS['text']};"),
                    output_widget("advanced_chart"),
                    class_="card",
                    style="margin-top: 1.5rem;"
                ),
                
                style="padding: 2rem;"
            )
        )
    )
)

