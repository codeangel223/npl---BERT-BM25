FROM python:3.10-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# COPY elastic-setup/ ./elastic-setup/

CMD ["python", "-m", "run"]
