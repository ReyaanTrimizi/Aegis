"""
AEGIS Data Module
Data generation and metric calculations
"""

import pandas as pd
import numpy as np


def generate_equipment_data():
    """Generate deterministic dataset of 20 defense equipment upgrades."""
    np.random.seed(42)
    
    equipment_names = [
        "M1 Abrams Tank Modernization",
        "F-35 Avionics Upgrade",
        "Aegis Combat System Enhancement",
        "M4 Carbine Replacement Program",
        "CH-47 Chinook Rotor Upgrade",
        "THAAD Radar Modernization",
        "Bradley Fighting Vehicle Armor",
        "V-22 Osprey Engine Overhaul",
        "Patriot Missile System Update",
        "Amphibious Assault Vehicle Refit",
        "F/A-18 Weapons Integration",
        "Satellite Communication Array",
        "Apache Helicopter Targeting System",
        "Naval Strike Missile Program",
        "Tactical Data Link Upgrade",
        "M777 Howitzer Precision Kit",
        "C-130 Hercules Modernization",
        "Submarine Sonar Enhancement",
        "Joint Light Tactical Vehicle",
        "B-2 Stealth Coating Refresh"
    ]
    
    dept_assignments = [
        "Army", "Air Force", "Navy", "Army", "Army",
        "Army", "Army", "Marines", "Army", "Marines",
        "Navy", "Air Force", "Army", "Navy", "Air Force",
        "Army", "Air Force", "Navy", "Army", "Air Force"
    ]
    
    cat_assignments = [
        "Vehicles", "Aircraft", "Weapons", "Weapons", "Aircraft",
        "Weapons", "Vehicles", "Aircraft", "Weapons", "Vehicles",
        "Aircraft", "Communications", "Aircraft", "Weapons", "Communications",
        "Weapons", "Aircraft", "Communications", "Vehicles", "Aircraft"
    ]
    
    priority_assignments = [
        "Critical", "Critical", "Critical", "High", "High",
        "Critical", "Medium", "High", "Critical", "Medium",
        "High", "High", "Critical", "High", "Medium",
        "Medium", "Medium", "Critical", "High", "Medium"
    ]
    
    costs = np.array([75, 82, 68, 35, 58, 71, 45, 63, 77, 42, 
                      55, 48, 61, 52, 39, 28, 67, 79, 44, 84])
    
    rois = np.array([2.45, 2.52, 2.81, 2.18, 2.68, 2.95, 1.92, 2.24, 2.98, 1.89,
                     2.71, 2.47, 3.12, 2.23, 2.15, 1.87, 2.61, 3.27, 2.19, 2.79])
    
    maintenance_pcts = np.array([0.06, 0.07, 0.04, 0.05, 0.07, 0.05, 0.08, 0.06, 0.04, 0.09,
                                  0.06, 0.05, 0.07, 0.05, 0.07, 0.09, 0.06, 0.03, 0.08, 0.04])
    
    ages = np.array([8, 5, 12, 6, 9, 7, 14, 10, 11, 15,
                     7, 8, 6, 9, 13, 16, 10, 4, 12, 3])
    
    lifespans = np.array([18, 20, 22, 15, 19, 21, 16, 18, 20, 14,
                          19, 17, 21, 18, 16, 12, 19, 24, 15, 22])
    
    df = pd.DataFrame({
        'upgrade_id': [f'U{i:02d}' for i in range(1, 21)],
        'upgrade_name': equipment_names,
        'department': dept_assignments,
        'category': cat_assignments,
        'priority': priority_assignments,
        'cost_m': costs,
        'roi': rois,
        'maintenance_pct': maintenance_pcts,
        'age_years': ages,
        'lifespan_years': lifespans,
    })
    
    return df


def calculate_metrics(df):
    """Calculate derived metrics for equipment portfolio."""
    if df.empty:
        return df
    
    df = df.copy()
    df['total_ownership_cost'] = df['cost_m'] * (1 + df['maintenance_pct'] * df['lifespan_years'])
    df['lifetime_return'] = df['cost_m'] * df['roi']
    df['net_value'] = df['lifetime_return'] - df['total_ownership_cost']
    df['value_score'] = df['net_value'] / df['cost_m']
    
    return df


# Generate base dataset on module load
BASE_DATA = calculate_metrics(generate_equipment_data())

