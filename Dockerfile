FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV ELASTIC_LOGGING_CONFIG_CONNECTION_STRING="http://10.100.18.155:30002"
ENV ELASTIC_LOGGING_CONFIG_INDEX_NAME="rpa-logs"
ENTRYPOINT ["python", "main.py"]

