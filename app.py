#!/usr/bin/env python3

from config import TELEGRAM_INIT_WEBHOOK_URL
import requests
from flask import Flask, request, jsonify
import bot
import json

app = Flask(__name__)
print(TELEGRAM_INIT_WEBHOOK_URL)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)

@app.route('/webhook', methods=['POST'])
def index():
    req = request.get_json()
    print(req)
    bot.send_message_to_chat_processor(req)
    return 'ok'

@app.route('/send_message/<string:idChat>', methods=['POST'])
def send_message(idChat):
    bot.send_message_to_user(idChat, request.get_data().decode('utf-8'))
    return 'ok'

@app.route('/send_photo/<string:idChat>', methods=['POST'])
def send_photo(idChat):
    json_object = json.loads(request.get_data().decode('utf-8'))
    photo_url = json_object['photo']
    caption = json_object['caption']
    bot.send_photo_to_user(idChat, photo_url, caption)
    return 'ok'

@app.route('/get_location/<string:idChat>', methods=['GET'])
def get_location(idChat):
    bot.get_location(idChat)
    return 'ok'

@app.route('/send_typing_act/<string:idChat>', methods['POST'])
def send_typing_action(idChat):
    bot.send_typing_action(idChat)
    return 'ok'


if __name__ == '__main__':
    app.run(port=5000)
