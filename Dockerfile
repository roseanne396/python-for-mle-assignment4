FROM python:3.11-slim

WORKDIR /app

# Install deps if present (won't fail if requirements.txt is empty/missing)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || true

# Copy the rest of the repo
COPY . /app

# Run the script (not a server)
CMD ["python", "app.py"]
