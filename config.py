import os

BOT_TOKEN = os.getenv('BOT_TOKEN', '')
NGROK_URL = os.getenv('NGROK_URL', '')
CHAT_PROCESSOR_URL = os.getenv('CHAT_PROCESSOR_URL', 'http://localhost:5001')
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
BASE_TELEGRAM_API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}&parse_mode={}&disable_notification={}'
TELEGRAM_SEND_MESSAGE_URL_BASE = BASE_TELEGRAM_API_URL + '/sendMessage'
TELEGRAM_SEND_PHOTO_URL = BASE_TELEGRAM_API_URL + '/sendPhoto?chat_id={}&photo={}&caption={}&parse_mode={}'
TELEGRAM_SEND_AUDIO_URL = BASE_TELEGRAM_API_URL + '/sendAudio?chat_id={}&audio={}&caption={}&parse_mode={}'
TELEGRAM_SEND_REPLY_MARKUP_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}&reply_markup={}'
TELEGRAM_SEND_TYPING_ACTION = BASE_TELEGRAM_API_URL + '/sendChatAction?chat_id={}&action={}'
