FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY log_parser.py .
COPY api_server.py .
COPY access.log .

RUN python3 log_parser.py

EXPOSE 5000

CMD ["python3", "api_server.py"]
