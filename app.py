from config import TELEGRAM_INIT_WEBHOOK_URL
import requests
from flask import Flask, request, jsonify
from bot import Bot

app = Flask(__name__)
print(TELEGRAM_INIT_WEBHOOK_URL)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    print(req)
    bot = Bot()
    bot.parse_data(req)
    success = bot.action()
    #return jsonify(success=success) # not enough
    return 'ok'

if __name__ == '__main__':
    app.run(port=8000)
