# Contributing to AEGIS

Thank you for your interest in contributing to AEGIS!

## Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Aegis.git`
3. Create a virtual environment: `python3 -m venv venv`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a feature branch: `git checkout -b feature/your-feature-name`

## Development Guidelines

### Code Style
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and single-purpose

### Project Structure
- `config.py` - Configuration constants
- `data.py` - Data generation and metrics
- `utils.py` - Helper functions
- `styles.py` - CSS styling
- `ui.py` - UI components
- `server.py` - Server logic
- `app.py` - Application entry point

### Testing
- Test locally before submitting: `shiny run app.py`
- Ensure all imports work correctly
- Check for linter errors

## Submitting Changes

1. Commit your changes with clear messages
2. Push to your fork
3. Submit a Pull Request with:
   - Clear description of changes
   - Screenshots if UI changes
   - Reference to related issues

## Reporting Issues

When reporting issues, please include:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Python version and OS

## Feature Requests

We welcome feature requests! Please:
- Check existing issues first
- Provide clear use case
- Explain expected behavior
- Consider implementation complexity

## Questions?

Open an issue with the "question" label.

