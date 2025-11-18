FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY config.py .
COPY data.py .
COPY utils.py .
COPY styles.py .
COPY ui.py .
COPY server.py .
COPY app.py .

# Expose port
EXPOSE 7860

# Run the application
CMD ["shiny", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]

