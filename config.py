BOT_TOKEN = ''
NGROK_URL = ''
CHAT_PROCESSOR_URL = 'http://localhost:5001'
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
BASE_TELEGRAM_API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}&parse_mode={}'
TELEGRAM_SEND_MESSAGE_URL_BASE = BASE_TELEGRAM_API_URL + '/sendMessage'
TELEGRAM_SEND_PHOTO_URL = BASE_TELEGRAM_API_URL + '/sendPhoto?chat_id={}&photo={}&caption={}&parse_mode={}'
TELEGRAM_SEND_AUDIO_URL = BASE_TELEGRAM_API_URL + '/sendAudio?chat_id={}&audio={}&caption={}&parse_mode={}'
