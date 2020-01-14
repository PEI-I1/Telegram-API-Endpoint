#!/usr/bin/env python3

from config import TELEGRAM_INIT_WEBHOOK_URL, msgs
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
    if "message" in req:
        if "text" in req["message"]:
            if req["message"]["text"] == '/start' or req["message"]["text"] == '/help':
                idChat = req["message"]["chat"]["id"]
                bot.send_message_to_user(idChat, msgs[req["message"]["text"]])
            else:
                bot.send_message_to_chat_processor(req)
        elif "location" in req["message"]:
            bot.send_message_to_chat_processor(req)
    elif "callback_query" in req:
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

@app.route('/send_keyboard/<string:idChat>', methods=['POST'])
def send_keyboard(idChat):
    json_object = json.loads(request.get_data().decode('utf-8'))
    text = json_object['text']
    keyboard = json_object['keyboard']
    bot.send_keyboard_to_user(idChat, text, keyboard)
    return 'ok'

@app.route('/get_location/<string:idChat>', methods=['GET'])
def get_location(idChat):
    bot.get_location(idChat)
    return 'ok'

@app.route('/send_typing_act/<string:idChat>', methods=['POST'])
def send_typing_action(idChat):
    bot.send_typing_action(idChat)
    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
