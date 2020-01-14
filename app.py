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
    if "message" in req and "text" in req["message"] and (req["message"]["text"] == '/start' or req["message"]["text"] == '/help'):
        command = req["message"]["text"]
        if command == '/start':
            idChat = req["message"]["chat"]["id"]
            bot.send_message_to_user(
                idChat, 
                'Olá! Sou o Bot da NOS!\n' +
                'Posso-te ajudar com informações sobre <b>cinemas</b>, <b>serviços da NOS</b> e <b>resolução de problemas técnicos</b>.\n' +
                'Para mais informações sobre mim utiliza o comando /help.\n' +
                'Caso encontres uma situação de erro ou desejes reiniciar a interação utiliza o comando /reset.\n' +
                'Em que te posso ser útil?'    
            )
        elif command == '/help':
            idChat = req["message"]["chat"]["id"]
            bot.send_message_to_user(
                idChat, 
                'Este bot pode ser dividido em 3 categorias:\n' + 
                '* <b>Cinemas</b>: permite a procura de cinemas perto de si, assim como a procura e a obtenção de informações sobre filmes e sessões, consoante variados critérios.\n' +
                '* <b>Serviços da NOS</b>: permite a procura de linhas de apoio, telemóveis para venda, tarifários WTF, pacotes da NOS (como satélite ou fibra), assim como a procura de lojas da NOS.\n' +
                '* <b>Resolução de problemas técnicos</b>: permite obter sugestões para resolver os problemas técnicos dos clientes da NOS.\n\n' +
                'Para além disto, o bot contém ainda um <b>modo interativo</b> que permite guiar o processo de obtenção de informações por parte do utilizador. Para entar neste modo basta enviar uma mensagem como \'modo regras\'.'    
            )
    # only tries to answer to user if user sends text or location
    elif ("message" in req and ("location" in req["message"] or "text" in req["message"])) or "callback_query" in req:
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
