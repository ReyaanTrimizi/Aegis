# AEGIS - Defense Equipment Portfolio Analyzer

[![Live Demo](https://img.shields.io/badge/Live%20Demo-shinyapps.io-blue)](https://reyaan.shinyapps.io/aegis_portfolio_analyzer/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A professional web application for analyzing defense equipment upgrade portfolios with budget optimization and value assessment capabilities.

## 🚀 Live Demo

**[View Live Application →](https://reyaan.shinyapps.io/aegis_portfolio_analyzer/)**

> **Note:** This is a **learning and demonstration project**. All data is simulated and does not represent actual defense equipment or portfolios. Built to demonstrate data visualization, interactive dashboards, and full-stack Python development skills.

## Features

- **Interactive Filtering** - Filter by department, category, priority, budget, and ROI
- **Real-time Metrics** - Live calculation of portfolio statistics
- **Multiple Chart Types** - Bar, scatter, box plot, and histogram visualizations
- **Custom Charts** - JSON-based chart configuration for advanced users
- **Professional UI** - Modern dark theme with responsive design

## Quick Start

1. **Install Python 3.8 or higher**

2. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   shiny run app.py --reload
   ```

5. **Open browser**
   Navigate to `http://127.0.0.1:8000`

## Project Structure

```
Aegis/
├── app.py          # Main entry point
├── config.py       # Configuration and constants
├── data.py         # Data generation and metrics
├── utils.py        # Helper functions
├── styles.py       # CSS styling
├── ui.py           # UI definition
├── server.py       # Server logic
└── requirements.txt
```

## Data Model

The application analyzes 20 defense equipment upgrades with the following attributes:

**Base Fields:**
- Cost (millions)
- ROI multiplier
- Maintenance percentage
- Age and lifespan (years)
- Department, category, priority

**Calculated Metrics:**
- Total Ownership Cost = Cost × (1 + Maintenance × Lifespan)
- Lifetime Return = Cost × ROI
- Net Value = Lifetime Return - Total Ownership Cost
- Value Score = Net Value / Cost

## Usage

### Dashboard Tab
- Use sidebar filters to narrow down equipment
- View summary metrics in cards
- Customize and generate charts
- Browse detailed data table

### Custom Charts Tab
- Edit JSON configuration
- Supports all chart types
- Flexible field mapping
- Real-time validation

## Technical Stack

- **Framework:** Shiny for Python
- **Visualization:** Plotly
- **Data Processing:** Pandas, NumPy
- **Styling:** Custom CSS with dark theme

## Deployment

### Docker Deployment

```bash
# Build the Docker image
docker build -t aegis-app .

# Run locally
docker run -p 8000:7860 aegis-app

# Access at http://localhost:8000
```

### Cloud Deployment Options

**Hugging Face Spaces (FREE)**
- Upload files to a new Space
- Use the provided Dockerfile
- Automatic deployment

**Render.com**
- Build: `pip install -r requirements.txt`
- Start: `shiny run app.py --host 0.0.0.0 --port $PORT`

**Docker-based Platforms**
- AWS ECS/Fargate
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform

## Repository

**GitHub:** [https://github.com/reyaantrimizi/Aegis](https://github.com/reyaantrimizi/Aegis)

## Contributing

This is a production application. For feature requests or issues, please open an issue on GitHub.

## Version History

- **v1.0** (Current) - Production release with full dashboard, filtering, and custom chart builder

## License

Demonstration application for portfolio analysis.

## Author

Reyaan Trimizi
