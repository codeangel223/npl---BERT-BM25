FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY elastic-setup/ ./elastic-setup/

CMD ["python", "elastic-setup/index_data.py"]
