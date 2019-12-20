import requests
from config import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_MESSAGE_URL_BASE, TELEGRAM_SEND_PHOTO_URL, TELEGRAM_SEND_AUDIO_URL, CHAT_PROCESSOR_URL, TELEGRAM_SEND_TYPING_ACTION
import json

def send_message_to_chat_processor(req):
    data = {}
    message = req['message']

    data['idChat'] = message['chat']['id'] # ID of Telegram chat
    data['idUser'] = message['from']['id'] # ID of Telegram user

    # Message received on Telegram chat
    if 'text' in message:
        data['msg'] = str(message['text'].encode('utf-8'), encoding='utf-8')
    else:
        data['msg'] = ''

    # Name of the user 
    data['name'] = message['from']['first_name'] 
    if 'last_name' in message['from']:
        data['name'] += " " + message['from']['last_name']

    # Location
    if 'location' in message:
        loc = message['location']
        data['location'] = {'lon': loc['longitude'], 'lat': loc['latitude']}
    else:
        data['location'] = None

    #Avisa chat_processor que chegou uma nova msg
    res = requests.post(CHAT_PROCESSOR_URL + "/getResponse", json=data)

def send_message_to_user(idChat, msg):
    res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(idChat, msg, 'HTML'))
    if res.status_code == 200:
        return True
    else:
        return False

def send_photo_to_user(idChat, photo_url, caption):
    res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(idChat, photo_url, caption, 'HTML'))
    if res.status_code == 200:
        return True
    else:
        return False

def send_typing_action(idChat):
    res = requests.get(TELEGRAM_SEND_TYPING_ACTION.format(idChat, 'typing'))
    
    
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
