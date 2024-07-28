FROM python:3.9-slim
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . .

# Expose port 7860 for Gradio
EXPOSE 7860

# Run the application
CMD ["python", "app.py"]