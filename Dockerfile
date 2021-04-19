FROM python:3.8-slim

COPY requirements.txt .

RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt 

WORKDIR /app

COPY ./app ./app
EXPOSE 8000
ENV PORT=8000
# FastAPIを8000ポートで待機
CMD uvicorn app.main:app --reload --host 0.0.0.0 --port $PORT 