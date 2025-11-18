"""
AEGIS Configuration
Constants, field definitions, and display names
"""

# Color palette
COLORS = {
    'background': '#0a0e1a',
    'panel': '#161b2e',
    'panel_light': '#1e2539',
    'border': '#2d3548',
    'text': '#f5f7fa',
    'text_secondary': '#b4bcd0',
    'accent_blue': '#4c9aff',
    'accent_green': '#36d399',
    'accent_orange': '#ff9f43',
    'accent_red': '#ff5e6c',
    'accent_purple': '#9c6ade',
}

DEPARTMENT_COLORS = {
    'Army': '#36d399',
    'Navy': '#4c9aff',
    'Air Force': '#9c6ade',
    'Marines': '#ff5e6c',
}

CATEGORY_COLORS = {
    'Vehicles': '#36d399',
    'Aircraft': '#4c9aff',
    'Communications': '#ff9f43',
    'Weapons': '#ff5e6c',
}

PRIORITY_COLORS = {
    'Critical': '#ff5e6c',
    'High': '#ff9f43',
    'Medium': '#4c9aff',
}

# Field definitions
NUMERIC_FIELDS = [
    "cost_m", "roi", "maintenance_pct", "age_years",
    "lifespan_years", "total_ownership_cost",
    "lifetime_return", "net_value", "value_score"
]

CATEGORICAL_FIELDS = ["upgrade_name", "department", "category", "priority"]
COLOR_OPTIONS = ["None", "department", "category", "priority"]

# Display names
FIELD_DISPLAY_NAMES = {
    "upgrade_name": "Equipment Name",
    "department": "Department",
    "category": "Category",
    "priority": "Priority Level",
    "cost_m": "Initial Cost ($M)",
    "roi": "Return on Investment",
    "maintenance_pct": "Maintenance Rate (%)",
    "age_years": "Age (Years)",
    "lifespan_years": "Lifespan (Years)",
    "total_ownership_cost": "Total Ownership Cost ($M)",
    "lifetime_return": "Lifetime Return ($M)",
    "net_value": "Net Value ($M)",
    "value_score": "Value Score"
}

COLOR_DISPLAY_NAMES = {
    "None": "No Color",
    "department": "By Department",
    "category": "By Category",
    "priority": "By Priority"
}

