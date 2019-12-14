from config import TELEGRAM_INIT_WEBHOOK_URL
import requests
from flask import Flask, request, jsonify
from bot import Bot

app = Flask(__name__)
print(TELEGRAM_INIT_WEBHOOK_URL)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)
bot = Bot()

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    print(req)
    bot.parse_data(req)
    success = bot.action()
    return 'ok'

if __name__ == '__main__':
    app.run(port=5000)
