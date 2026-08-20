#!/usr/bin/env python3
import sqlite3
import urllib.request
import urllib.parse
import json

# Данные бота (необходимо указать данные или оставить тестовые)
TELEGRAM_BOT_TOKEN = "TEST_BOT_TOKEN"
TELEGRAM_CHAT_ID = "12345678"
DB_FILE = "logs.db"

def check_errors_and_alert():
    """ Проверяет наличие критических ошибок 500 в базе и отправляет алерт """
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # Запрос SQL: считаем количество ошибок 500
    cursor.execute("SELECT COUNT(*) FROM access_logs WHERE status_code = 500")
    error_count = cursor.fetchone()[0]
    conn.close()
    
    print(f"[INFO] Найдено критических ошибок 500 в базе: {error_count}")
    
    if error_count > 0:
        alert_text = f" ALERT! На сервере обнаружено {error_count} критических ошибок 500!"
        print(f"[ALERTING] Формируем отправку алерта: '{alert_text}'")
        
        # Если указан реальный токен бота — отправляем запрос в Telegram API
        if TELEGRAM_BOT_TOKEN != "TEST_BOT_TOKEN":
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            params = urllib.parse.urlencode({"chat_id": TELEGRAM_CHAT_ID, "text": alert_text}).encode("utf-8")
            try:
                req = urllib.request.Request(url, data=params)
                with urllib.request.urlopen(req) as response:
                    print("[SUCCESS] Уведомление успешно отправлено в Telegram!")
            except Exception as e:
                print(f"[ERROR] Не удалось отправить алерт: {e}")
        else:
            print("[SIMULATION] Имитация отправки в Telegram прошла успешно!")
    else:
        print("[OK] Ошибок 500 не обнаружено, отправка алерта не требуется.")

if __name__ == "__main__":
    check_errors_and_alert()
