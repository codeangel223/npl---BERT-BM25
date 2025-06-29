FROM python:3.12-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src
COPY run/ ./run

CMD ["python", "-m", "run"]

# docker build -t bm25_and_bert_project .