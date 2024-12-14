# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app 

# Copy application files to the container
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
