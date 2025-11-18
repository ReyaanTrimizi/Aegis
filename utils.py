"""
AEGIS Utility Functions
Chart creation, filtering, and parsing logic
"""

import plotly.express as px
import plotly.graph_objects as go
import re
from config import (
    COLORS, DEPARTMENT_COLORS, CATEGORY_COLORS, PRIORITY_COLORS,
    FIELD_DISPLAY_NAMES, NUMERIC_FIELDS, CATEGORICAL_FIELDS
)


def filter_data(df, departments, categories, priorities, max_budget, min_roi):
    """Apply filters to the dataset."""
    filtered = df.copy()
    
    if departments:
        filtered = filtered[filtered['department'].isin(departments)]
    if categories:
        filtered = filtered[filtered['category'].isin(categories)]
    if priorities:
        filtered = filtered[filtered['priority'].isin(priorities)]
    
    filtered = filtered[filtered['cost_m'] <= max_budget]
    filtered = filtered[filtered['roi'] >= min_roi]
    
    return filtered


def create_chart(df, chart_type, x_field, y_field, color_field, show_trendline=False):
    """Create plotly chart based on type and configuration."""
    if df.empty:
        fig = go.Figure()
        fig.add_annotation(
            text="No data available for selected filters",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=18, color=COLORS['text'])
        )
        apply_dark_theme(fig)
        return fig
    
    # Handle color mapping
    color_map = None
    if color_field and color_field != "None":
        if color_field == "department":
            color_map = DEPARTMENT_COLORS
        elif color_field == "category":
            color_map = CATEGORY_COLORS
        elif color_field == "priority":
            color_map = PRIORITY_COLORS
    
    color_col = None if color_field == "None" else color_field
    x_display = FIELD_DISPLAY_NAMES.get(x_field, x_field)
    y_display = FIELD_DISPLAY_NAMES.get(y_field, y_field)
    
    try:
        if chart_type == "Bar Chart":
            if y_field not in NUMERIC_FIELDS:
                return create_error_chart("Bar chart requires a numeric Y-axis field")
            
            plot_df = df.sort_values(y_field, ascending=False)
            fig = px.bar(
                plot_df, x=x_field, y=y_field, color=color_col,
                color_discrete_map=color_map,
                title=f"{y_display} by {x_display}",
                labels={x_field: x_display, y_field: y_display}
            )
            
        elif chart_type == "Scatter Plot":
            if x_field not in NUMERIC_FIELDS or y_field not in NUMERIC_FIELDS:
                return create_error_chart("Scatter plot requires numeric fields for both X and Y axes.<br>Please select numeric fields like Cost, ROI, Age, etc.")
            
            trendline_param = None
            if show_trendline:
                if x_field == y_field:
                    return create_error_chart("Trendline cannot be shown when X and Y are the same field.<br>Please select different fields for X and Y axes.")
                
                try:
                    import statsmodels.api as sm
                    trendline_param = "ols"
                except ImportError:
                    return create_error_chart("Trendline requires the 'statsmodels' package.<br>Run: pip install statsmodels")
            
            fig = px.scatter(
                df, x=x_field, y=y_field, color=color_col,
                color_discrete_map=color_map,
                title=f"{y_display} vs {x_display}",
                trendline=trendline_param,
                labels={x_field: x_display, y_field: y_display}
            )
            
        elif chart_type == "Box Plot":
            if x_field not in CATEGORICAL_FIELDS or y_field not in NUMERIC_FIELDS:
                return create_error_chart("Box plot requires:<br>• X-axis: Categorical field (Department, Category, Priority, or Equipment Name)<br>• Y-axis: Numeric field (Cost, ROI, Value Score, etc.)")
            
            fig = px.box(
                df, x=x_field, y=y_field, color=color_col,
                color_discrete_map=color_map,
                title=f"{y_display} Distribution by {x_display}",
                labels={x_field: x_display, y_field: y_display}
            )
            
        elif chart_type == "Histogram":
            if x_field not in NUMERIC_FIELDS:
                return create_error_chart("Histogram requires a numeric X-axis field.<br>Please select fields like Cost, ROI, Age, Value Score, etc.")
            
            fig = px.histogram(
                df, x=x_field, color=color_col,
                color_discrete_map=color_map, nbins=15,
                title=f"Distribution of {x_display}",
                labels={x_field: x_display}
            )
        else:
            return create_error_chart("Unknown chart type")
        
        apply_dark_theme(fig)
        return fig
        
    except Exception as e:
        return create_error_chart(f"Error: {str(e)}")


def create_error_chart(message):
    """Create an error message chart."""
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        xref="paper", yref="paper",
        x=0.5, y=0.5, showarrow=False,
        font=dict(size=16, color=COLORS['accent_red'], family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif")
    )
    apply_dark_theme(fig)
    return fig


def apply_dark_theme(fig):
    """Apply consistent dark theme to plotly figure."""
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=COLORS['panel'],
        plot_bgcolor=COLORS['background'],
        font=dict(color=COLORS['text'], size=13, family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"),
        title_font=dict(size=16, color=COLORS['text'], family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"),
        margin=dict(l=70, r=40, t=60, b=70),
        height=550,
        hoverlabel=dict(
            bgcolor=COLORS['panel_light'],
            font_size=13,
            font_color=COLORS['text'],
            font_family="Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
        )
    )
    fig.update_xaxes(
        gridcolor=COLORS['border'], showgrid=True,
        title_font=dict(size=14, color=COLORS['text']),
        tickfont=dict(size=12, color=COLORS['text'])
    )
    fig.update_yaxes(
        gridcolor=COLORS['border'], showgrid=True,
        title_font=dict(size=14, color=COLORS['text']),
        tickfont=dict(size=12, color=COLORS['text'])
    )


def format_currency(value):
    """Format value as currency in millions."""
    return f"${value:.1f}M"


def parse_simple_text(text):
    """Parse simple text input into chart configuration."""
    text = text.lower().strip()
    
    config = {
        'chart_type': 'Bar Chart',
        'x_axis': 'department',
        'y_axis': 'cost_m',
        'color_by': 'None',
        'show_trendline': False
    }
    
    if 'scatter' in text:
        config['chart_type'] = 'Scatter Plot'
    elif 'box' in text:
        config['chart_type'] = 'Box Plot'
    elif 'histogram' in text or 'distribution' in text:
        config['chart_type'] = 'Histogram'
    elif 'bar' in text:
        config['chart_type'] = 'Bar Chart'
    
    if 'trendline' in text or 'trend' in text:
        config['show_trendline'] = True
    
    if 'cost' in text and 'ownership' not in text:
        if 'x' in text or text.index('cost') < len(text) / 2:
            config['x_axis'] = 'cost_m'
        else:
            config['y_axis'] = 'cost_m'
    
    if 'roi' in text or 'return' in text:
        if 'vs' in text or 'against' in text:
            config['y_axis'] = 'roi'
        else:
            config['x_axis'] = 'roi'
    
    if 'value score' in text or 'value' in text:
        config['y_axis'] = 'value_score'
    
    if 'age' in text:
        config['x_axis'] = 'age_years'
    
    if 'maintenance' in text:
        config['y_axis'] = 'maintenance_pct'
    
    if 'colored by department' in text or 'color department' in text or 'by department' in text:
        config['color_by'] = 'department'
    elif 'colored by category' in text or 'color category' in text or 'by category' in text:
        config['color_by'] = 'category'
    elif 'colored by priority' in text or 'color priority' in text or 'by priority' in text:
        config['color_by'] = 'priority'
    
    match = re.search(r'(?:of|plot)\s+(\w+(?:\s+\w+)?)\s+(?:and|vs)\s+(\w+(?:\s+\w+)?)', text)
    if match:
        field1 = match.group(1).strip()
        field2 = match.group(2).strip()
        
        if 'value' in field1:
            config['x_axis'] = 'value_score'
        if 'age' in field2:
            config['y_axis'] = 'age_years'
    
    return config


def validate_chart_config(config):
    """Validate chart configuration."""
    errors = []
    
    valid_charts = ['Bar Chart', 'Scatter Plot', 'Box Plot', 'Histogram']
    if config.get('chart_type') not in valid_charts:
        errors.append(f"Invalid chart type. Must be one of: {', '.join(valid_charts)}")
    
    all_fields = CATEGORICAL_FIELDS + NUMERIC_FIELDS
    if config.get('x_axis') and config['x_axis'] not in all_fields:
        errors.append(f"Invalid x_axis field: {config['x_axis']}")
    if config.get('y_axis') and config['y_axis'] not in all_fields:
        errors.append(f"Invalid y_axis field: {config['y_axis']}")
    
    valid_colors = ['None', 'department', 'category', 'priority']
    if config.get('color_by') and config['color_by'] not in valid_colors:
        errors.append(f"Invalid color_by. Must be one of: {', '.join(valid_colors)}")
    
    return errors

