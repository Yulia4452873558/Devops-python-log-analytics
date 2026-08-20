#!/usr/bin/env python3
import sqlite3
import re

LOG_FILE = "access.log"
DB_FILE = "logs.db"

def init_db():
    conn = sqlite3.connect("logs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS access_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip_address TEXT,
            http_method TEXT,
            request_url TEXT,
            status_code INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def parse_and_save_logs():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    with open(LOG_FILE, "r") as f:
         for line in f:
             match = re.search(r'(\d+\.\d+\.\d+\.\d+).*?"([A-Z]+) (.*?) HTTP/.*?" (\d+)', line)
             if match:
                 ip =  match.group(1)
                 method = match.group(2)
                 url = match.group(3)
                 status = int(match.group(4))

                 cursor.execute(
                    "INSERT INTO access_logs (ip_address, http_method, request_url, status_code) VALUES (?, ?, ?, ?)",
                    (ip, method, url, status)
                )
    conn.commit()
    conn.close()
    print("[SUCCESS] Логи успешно распарсены и сохранены в базу данных SQL!")

if __name__ == "__main__":
   init_db()
   print("База данных успешно создана!")
   parse_and_save_logs()
