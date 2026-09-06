# DevOps Python Log Analytics & Dockerized Infrastructure

![Python](https://img.shields.io/badge/Language-Python%203-blue)
![Flask](https://img.shields.io/badge/Framework-Flask%20REST%20API-black)
![SQLite](https://img.shields.io/badge/Database-SQLite%203-blue)
![Nginx](https://img.shields.io/badge/Web%20Server-Nginx%20Reverse%20Proxy-green)
![Docker](https://img.shields.io/badge/Container-Docker%20Compose-blue)
![Alerting](https://img.shields.io/badge/Alerts-Telegram%20Bot%20API-blue)

An end-to-end DevOps log analytics pipeline built with Python, SQLite, Flask, Nginx, and Docker. It parses Nginx access logs, stores metrics in an SQL database, exposes a REST API via a Flask microservice behind an Nginx Reverse Proxy, triggers automated Telegram alerts on 5xx errors, and is fully containerized using Docker Compose.

---

## 🏗 Architecture Diagram

```text
[ Nginx Access Logs ]
        │
        ▼
[ log_parser.py ] ──► [ SQLite DB (logs.db) ]
                              │
                              ▼
[ Nginx (Port 8085) ] ──► [ api_server.py (Port 5000) ] ──► [ telegram_alert.py ]
  (Reverse Proxy)              (Flask REST API)                 (Alerting Engine)
        │                             │
        └──────────────┬──────────────┘
                       ▼
            [ Docker Compose Stack ]
---

🚀 Components

1. Log Parser (log_parser.py): Regex-based parser that reads access.log and populates the SQLite database (access_logs table).

2. REST API Microservice (api_server.py): Flask web server running on port 5000 exposing GET /metrics returning JSON metrics.

3. Nginx Reverse Proxy (nginx_log_analytics.conf): Nginx server listening on port 8085 forwarding client requests to the Flask app on port 5000.

4. Telegram Alert Engine (telegram_alert.py): Queries SQLite for 500 HTTP errors and dispatches alerts via Telegram Bot API.

5. Docker Stack (docker-compose.yml): Multi-container orchestration managing api and webproxy containers.

---

💻 Quick Start & Testing
1. Launch the entire containerized stack with 1 command:
docker compose up -d

2. Test API via Nginx Reverse Proxy (Port 8085):
curl -s http://localhost:8085/metrics | jq .

3. Trigger Telegram Error Alert Check:
chmod +x telegram_alert.py
./telegram_alert.py
