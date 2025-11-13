# Step 1: Use an official lightweight Python image
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy all project files into the container
COPY . .

# Step 5: Expose the port your app runs on
EXPOSE 5000

# Step 6: Run the application
CMD ["python", "app.py"]
