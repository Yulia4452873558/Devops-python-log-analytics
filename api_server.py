#!/usr/bin/env python3
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "logs.db"

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """ Эндпоинт отдает статистику по логам в формате JSON """
    conn = get_db_connection()
    cursor = conn.cursor()

    """Запросы на языке SQL (используем  колонку status_code) """
    total = cursor.execute("SELECT COUNT(*) FROM access_logs").fetchone()[0]
    errors_500 = cursor.execute(
        "SELECT COUNT(*) FROM access_logs WHERE status_code = 500"
    ).fetchone()[0]
    errors_404 = cursor.execute(
        "SELECT COUNT(*) FROM access_logs WHERE status_code = 404"
    ).fetchone()[0]

    conn.close()

    return jsonify(
      {
           "status": "success",
           "total_request": total,
           "errors_500": errors_500,
           "errors_404": errors_404,
      }
)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
