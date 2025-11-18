"""
AEGIS Styles
CSS styling for the application
"""

from config import COLORS


def get_custom_css():
    """Return custom CSS for the application."""
    return f"""
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            background-color: {COLORS['background']} !important;
            color: {COLORS['text']};
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.5;
        }}
        .navbar {{
            background: linear-gradient(135deg, {COLORS['panel']} 0%, {COLORS['panel_light']} 100%);
            border-bottom: 2px solid {COLORS['border']};
            padding: 2rem 2.5rem;
            box-shadow: 0 4px 16px rgba(0,0,0,0.4);
        }}
        .header-container {{
            display: flex;
            align-items: center;
            gap: 1.5rem;
        }}
        .header-title {{
            font-size: 3.5rem;
            font-weight: 800;
            letter-spacing: 4px;
            margin: 0;
            background: linear-gradient(135deg, {COLORS['accent_blue']}, {COLORS['accent_purple']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            flex-shrink: 0;
        }}
        .header-content {{
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}
        .header-subtitle {{
            font-size: 1.2rem;
            font-weight: 600;
            color: {COLORS['text']};
            margin: 0;
            line-height: 1.3;
        }}
        .header-description {{
            font-size: 0.95rem;
            color: {COLORS['text_secondary']};
            margin: 0;
            line-height: 1.3;
        }}
        .sidebar {{
            background-color: {COLORS['panel']} !important;
            border-right: 1px solid {COLORS['border']};
            padding: 1.5rem;
            height: 100vh;
            overflow-y: auto;
        }}
        .card {{
            background-color: {COLORS['panel']};
            border: 1px solid {COLORS['border']};
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }}
        .metric-card {{
            background: linear-gradient(135deg, {COLORS['panel']} 0%, {COLORS['panel_light']} 100%);
            border: 1px solid {COLORS['border']};
            border-radius: 8px;
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.2s, box-shadow 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        .metric-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(91, 156, 245, 0.2);
        }}
        .metric-value {{
            font-size: 2.5rem;
            font-weight: 800;
            color: {COLORS['accent_blue']};
            margin: 0.75rem 0;
            letter-spacing: -0.5px;
            text-shadow: 0 2px 4px rgba(76, 154, 255, 0.3);
        }}
        .metric-label {{
            font-size: 0.8rem;
            font-weight: 700;
            color: {COLORS['text']};
            text-transform: uppercase;
            letter-spacing: 1.2px;
        }}
        .btn-primary {{
            background: linear-gradient(135deg, {COLORS['accent_blue']}, {COLORS['accent_purple']});
            border: none;
            color: white !important;
            padding: 0.75rem 1.25rem;
            border-radius: 8px;
            margin: 0.35rem 0;
            width: 100%;
            font-weight: 700;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(76, 154, 255, 0.3);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .btn-primary:hover {{
            background: linear-gradient(135deg, #3d8aef, #8a5dd1);
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(76, 154, 255, 0.5);
        }}
        .btn-primary:active {{
            transform: translateY(0);
        }}
        .form-control, .form-select {{
            background-color: {COLORS['background']} !important;
            border: 1px solid {COLORS['border']} !important;
            color: {COLORS['text']} !important;
            border-radius: 6px;
            padding: 0.5rem 0.75rem;
            font-size: 0.875rem;
        }}
        .form-control:focus, .form-select:focus {{
            background-color: {COLORS['background']} !important;
            border-color: {COLORS['accent_blue']} !important;
            color: {COLORS['text']} !important;
            box-shadow: 0 0 0 3px rgba(91, 156, 245, 0.1) !important;
        }}
        .form-check-input {{
            background-color: {COLORS['background']};
            border: 2px solid {COLORS['border']};
            width: 1.25rem;
            height: 1.25rem;
            margin-right: 0.5rem;
            cursor: pointer;
        }}
        .form-check-input:checked {{
            background-color: {COLORS['accent_blue']};
            border-color: {COLORS['accent_blue']};
        }}
        .form-check-label {{
            color: {COLORS['text']} !important;
            font-size: 0.85rem;
            cursor: pointer;
            font-weight: 500;
            white-space: nowrap;
        }}
        .form-check {{
            margin-bottom: 0.5rem;
        }}
        .irs-single {{
            background-color: {COLORS['accent_blue']} !important;
            color: white !important;
            font-weight: 700 !important;
            font-size: 0.85rem !important;
        }}
        .form-group label {{
            color: {COLORS['text']} !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {COLORS['text']};
            font-weight: 600;
        }}
        h4 {{
            font-size: 1.4rem;
            margin-bottom: 1.25rem;
            color: {COLORS['text']};
            font-weight: 700;
            letter-spacing: 0.5px;
        }}
        label {{
            color: {COLORS['text']} !important;
            font-weight: 600;
            font-size: 0.85rem;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .section-title {{
            font-size: 0.8rem;
            font-weight: 700;
            color: {COLORS['text']} !important;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid {COLORS['accent_blue']};
        }}
        .table {{
            color: {COLORS['text']} !important;
            background-color: {COLORS['panel']};
            font-size: 0.875rem;
        }}
        .table thead {{
            background-color: {COLORS['panel_light']};
            border-bottom: 2px solid {COLORS['border']};
        }}
        .table thead th {{
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.75rem;
            letter-spacing: 0.5px;
            padding: 0.75rem;
            color: {COLORS['text']} !important;
        }}
        .table td {{
            padding: 0.75rem;
            border-bottom: 1px solid {COLORS['border']};
            color: {COLORS['text']} !important;
        }}
        .table tbody tr {{
            color: {COLORS['text']} !important;
        }}
        .table tbody tr:hover {{
            background-color: {COLORS['panel_light']};
        }}
        .shiny-data-grid {{
            background-color: {COLORS['panel']} !important;
            color: {COLORS['text']} !important;
        }}
        .shiny-data-grid table {{
            color: {COLORS['text']} !important;
        }}
        .shiny-data-grid th {{
            color: {COLORS['text']} !important;
            background-color: {COLORS['panel_light']} !important;
        }}
        .shiny-data-grid td {{
            color: {COLORS['text']} !important;
        }}
        .table-container {{
            max-height: 500px;
            overflow-y: auto;
            background-color: {COLORS['panel']};
            border: 1px solid {COLORS['border']};
            border-radius: 8px;
        }}
        ::-webkit-scrollbar {{
            width: 10px;
            height: 10px;
        }}
        ::-webkit-scrollbar-track {{
            background: {COLORS['background']};
        }}
        ::-webkit-scrollbar-thumb {{
            background: {COLORS['border']};
            border-radius: 5px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: {COLORS['text_secondary']};
        }}
        input[type="range"] {{
            -webkit-appearance: none;
            width: 100%;
            height: 8px;
            border-radius: 4px;
            background: linear-gradient(to right, {COLORS['accent_blue']}, {COLORS['accent_purple']});
            outline: none;
            opacity: 0.8;
            transition: opacity 0.2s;
        }}
        input[type="range"]:hover {{
            opacity: 1;
        }}
        input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: {COLORS['text']};
            cursor: pointer;
            box-shadow: 0 0 10px rgba(76, 154, 255, 0.5);
            border: 3px solid {COLORS['accent_blue']};
        }}
        input[type="range"]::-moz-range-thumb {{
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: {COLORS['text']};
            cursor: pointer;
            border: 3px solid {COLORS['accent_blue']};
            box-shadow: 0 0 10px rgba(76, 154, 255, 0.5);
        }}
        input[type="range"]::-moz-range-track {{
            background: linear-gradient(to right, {COLORS['accent_blue']}, {COLORS['accent_purple']});
            border-radius: 4px;
            height: 8px;
        }}
        .irs {{
            font-family: inherit;
        }}
        .irs-bar {{
            background: linear-gradient(to right, {COLORS['accent_blue']}, {COLORS['accent_purple']}) !important;
            border: none !important;
            height: 8px !important;
        }}
        .irs-line {{
            background: {COLORS['border']} !important;
            border: none !important;
            height: 8px !important;
        }}
        .irs-handle {{
            background: {COLORS['text']} !important;
            border: 3px solid {COLORS['accent_blue']} !important;
            box-shadow: 0 0 10px rgba(76, 154, 255, 0.5) !important;
            width: 20px !important;
            height: 20px !important;
            top: 22px !important;
        }}
        .irs-handle:hover {{
            background: {COLORS['accent_blue']} !important;
        }}
        .irs-min, .irs-max {{
            color: {COLORS['text']} !important;
            background-color: {COLORS['panel_light']} !important;
            font-size: 0.75rem !important;
            font-weight: 600 !important;
            padding: 2px 6px !important;
            border-radius: 3px !important;
        }}
        .irs-from, .irs-to {{
            color: white !important;
            background-color: {COLORS['accent_blue']} !important;
        }}
        .chart-controls {{
            background-color: {COLORS['panel_light']};
            padding: 1rem;
            border-radius: 6px;
            margin-bottom: 1rem;
        }}
        .nav-pills .nav-link {{
            color: {COLORS['text']} !important;
            background-color: transparent !important;
            border: 1px solid {COLORS['border']};
            margin-right: 0.5rem;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            transition: all 0.2s;
        }}
        .nav-pills .nav-link:hover {{
            background-color: {COLORS['panel_light']} !important;
            border-color: {COLORS['accent_blue']};
        }}
        .nav-pills .nav-link.active {{
            background: linear-gradient(135deg, {COLORS['accent_blue']}, {COLORS['accent_purple']}) !important;
            border-color: transparent !important;
            color: white !important;
        }}
        .tab-content {{
            animation: fadeIn 0.3s ease-in;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    """

