import requests
from config import TELEGRAM_SEND_MESSAGE_URL, TELEGRAM_SEND_MESSAGE_URL_BASE, TELEGRAM_SEND_PHOTO_URL, TELEGRAM_SEND_AUDIO_URL, CHAT_PROCESSOR_URL, TELEGRAM_SEND_REPLY_MARKUP_URL, TELEGRAM_SEND_TYPING_ACTION
import json, urllib.parse

def send_message_to_chat_processor(req):
    data = {}

    if 'message' in req:
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

        # Timestamp
        data['timestamp'] = message['date']

        # Location
        if 'location' in message:
            loc = message['location']
            data['location'] = {'lon': loc['longitude'], 'lat': loc['latitude']}
        else:
            data['location'] = None

    else:
        message = req['callback_query']

        data['idChat'] = message['message']['chat']['id']
        data['idUser'] = message['from']['id']

        data['msg'] = str(message['data'].encode('utf-8'), encoding='utf-8')

        data['name'] = message['from']['first_name']
        if 'last_name' in message['from']:
            data['name'] += " " + message['from']['last_name']

        data['timestamp'] = message['message']['date']

        if 'location' in message['message']:
            loc = message['message']['location']
            data['location'] = {'lon': loc['longitude'], 'lat': loc['latitude']}
        else:
            data['location'] = None
    
    #Avisa chat_processor que chegou uma nova msg
    res = requests.post(CHAT_PROCESSOR_URL + "/getResponse", json=data)

def send_message_to_user(idChat, msg, disable_notification):
    msg = urllib.parse.quote(msg, safe='')
    res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(idChat, msg, 'HTML', disable_notification))
    if res.status_code == 200:
        return True
    else:
        return False

def send_photo_to_user(idChat, photo_url, caption):
    caption = urllib.parse.quote(caption, safe='')
    res = requests.get(TELEGRAM_SEND_PHOTO_URL.format(idChat, photo_url, caption, 'HTML'))
    if res.status_code == 200:
        return True
    else:
        return False

def send_keyboard_to_user(idChat, text, keyboard):
    res = requests.get(TELEGRAM_SEND_REPLY_MARKUP_URL.format(idChat, text, keyboard))
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
                'text': 'Enviar Localização',
                'request_location': True
            }]
        ]
    }
    
    payload = {
        'chat_id': idChat,
        'text': 'Clica no botão para me enviares a tua localização',
        'reply_markup': json.dumps(reply_markup)
    }

    res = requests.post(TELEGRAM_SEND_MESSAGE_URL_BASE, data=payload)

    if res.status_code == 200:
        return True
    else:
        return False
