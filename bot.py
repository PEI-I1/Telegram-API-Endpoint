import requests
from config import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_MESSAGE_URL_BASE, TELEGRAM_SEND_PHOTO_URL, TELEGRAM_SEND_AUDIO_URL, CHAT_PROCESSOR_URL
import json

class Bot:

    def __init__(self, req):
        message = req['message']

        self.chat = message['chat']['id'] # ID of Telegram chat
        self.user = message['from']['id'] # ID of Telegram user

        # Message received on Telegram chat
        if 'text' in message:
            self.message_received = str(message['text'].encode('utf-8'), encoding='utf-8')
        else:
            self.message_received = ''

        self.message_send = None        # Message to send to Telegram chat

        # Name of the user 
        self.name = message['from']['first_name'] 
        if 'last_name' in message['from']:
            self.name += " " + message['from']['last_name']

        # Location
        if 'location' in message:
            loc = message['location']
            self.location = {'lon': loc['longitude'], 'lat': loc['latitude']}
        else:
            self.location = None

    def get_response(self):
        data = {}
        data['idChat'] = str(self.chat)
        data['idUser'] = str(self.user)
        data['msg'] = self.message_received
        data['name'] = self.name
        data['location'] = self.location

        res = requests.post(CHAT_PROCESSOR_URL + "/getResponse", json=data)
        self.message_send = res.text

    def send_message(self):
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat, self.message_send, 'HTML'))
        if res.status_code == 200:
            return True
        else:
            return False

    def get_location(idChat):

        reply_markup={
            'keyboard': [
                [{
                    'text': 'Send Location',
                    'request_location': True
                }]
            ]
        }
        
        payload = {
            'chat_id': idChat,
            'text': 'Clique no botão em baixo para podermos saber onde está',
            'reply_markup': json.dumps(reply_markup)
        }

        res = requests.post(TELEGRAM_SEND_MESSAGE_URL_BASE, data=payload)

        if res.status_code == 200:
            return True
        else:
            return False
