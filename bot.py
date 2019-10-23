import requests
from config import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_MESSAGE_URL_BASE, TELEGRAM_SEND_PHOTO_URL, TELEGRAM_SEND_AUDIO_URL
import json

class Bot:

    def __init__(self):
        
        self.chat = None                # ID of Telegram chat
        self.message_received = None    # Message received on Telegram chat
        self.message_send = None        # Message to send to Telegram chat
        self.first_name = None          # First name of the user
    
    def send_message(self):

        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat, self.message_send))
        if res.status_code == 200:
            return True
        else:
            return False

    def get_location(self):

        reply_markup={
            'keyboard': [
                [{
                    'text': 'Send Location',
                    'request_location': True
                }]
            ]
        }
        
        payload = {
            'chat_id': self.chat,
            'text': 'Clique no botão em baixo para podermos saber onde está',
            'reply_markup': json.dumps(reply_markup)
        }

        res = requests.post(TELEGRAM_SEND_MESSAGE_URL_BASE, data=payload)

        if res.status_code == 200:
            return True
        else:
            return False

    def send_photo(self):

        res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(self.chat, 'https://www.himgs.com/imagenes/hello/social/hello-fb-logo.png', '<b>Just a photo</b>', 'HTML'))
        
        if res.status_code == 200:
            return True
        else:
            return False

    def send_audio(self):

        res = requests.get(TELEGRAM_SEND_AUDIO_URL.format(self.chat, 'http://soundbible.com/mp3/Hello-SoundBible.com-218208532.mp3', '<em>Just to say hello</em>', 'HTML'))
        if res.status_code == 200:
            return True
        else:
            return False
    
    def parse_data(self, data):
        
        message = data['message']

        self.chat = message['chat']['id']
        self.message_received = message['text'].lower()
        self.first_name = message['from']['first_name']

    def action(self):

        success = None

        if self.message_received in ['olá', 'hello']:
            self.message_send = 'Hello ' + self.first_name + '!'
            success = self.send_message()
        elif self.message_received in ['imagem', 'image']:
            success = self.send_photo()
        elif self.message_received in ['áudio', 'audio']:
            success = self.send_audio()
        elif self.message_received in ['localização', 'location']:
            success = self.get_location()
        else:
            self.message_send = 'What do you mean?'
            success = self.send_message()

        return success
