#  DevOps Python Log Analytics & Reverse Proxy Infrastructure

![Python](https://img.shields.io/badge/Language-Python%203-blue)
![Flask](https://img.shields.io/badge/Framework-Flask%20REST%20API-black)
![SQLite](https://img.shields.io/badge/Database-SQLite%203-blue)
![Nginx](https://img.shields.io/badge/Web%20Server-Nginx%20Reverse%20Proxy-green)
![Alerting](https://img.shields.io/badge/Alerts-Telegram%20Bot%20API-blue)

An end-to-end DevOps log analytics pipeline built with Python, SQLite, Flask, and Nginx. It parses Nginx access logs, stores metrics in an SQL database, exposes a REST API via a Flask microservice behind an Nginx Reverse Proxy, and triggers automated Telegram alerts on 5xx errors.

---

## 🏗 Architecture Diagram

```text
[ Nginx Access Logs ]
        │
        ▼
[ log_parser.py ] ──► [ SQLite DB (logs.db) ]
                              │
                              ▼
[ Nginx (Port 8080) ] ──► [ api_server.py (Port 5000) ] ──► [ telegram_alert.py ]
  (Reverse Proxy)              (Flask REST API)                 (Alerting Engine)
```

---

🚀 Components

    Log Parser (log_parser.py): Regex-based parser that reads access.log and populates the SQLite database (access_logs table).

    REST API Microservice (api_server.py): Flask web server running on port 5000 exposing GET /metrics returning JSON metrics.

    Nginx Reverse Proxy (nginx_log_analytics.conf): Nginx server listening on port 8080 forwarding client requests to the Flask app on port 5000.

    Telegram Alert Engine (telegram_alert.py): Queries SQLite for 500 HTTP errors and dispatches alerts via Telegram Bot API.

---

💻 Quick Start & Testing
1. Run Log Parser & Populate SQL DB
chmod +x log_parser.py
./log_parser.py

2. Start Python Flask API
chmod +x api_server.py
./api_server.py

3. Test API via Nginx Reverse Proxy (Port 8080)
curl -s http://localhost:8080/metrics | jq .

4. Trigger Telegram Error Alert Check
chmod +x telegram_alert.py
./telegram_alert.py
