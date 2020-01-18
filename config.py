import os

BOT_TOKEN = os.getenv('BOT_TOKEN', '')
NGROK_URL = os.getenv('NGROK_URL', '')
CHAT_PROCESSOR_URL = os.getenv('CHAT_PROCESSOR_URL', 'http://localhost:5001')
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
BASE_TELEGRAM_API_URL = 'https://api.telegram.org/bot' + BOT_TOKEN
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_API_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}&parse_mode={}'
TELEGRAM_SEND_MESSAGE_URL_BASE = BASE_TELEGRAM_API_URL + '/sendMessage'
TELEGRAM_SEND_PHOTO_URL = BASE_TELEGRAM_API_URL + '/sendPhoto?chat_id={}&photo={}&caption={}&parse_mode={}'
TELEGRAM_SEND_AUDIO_URL = BASE_TELEGRAM_API_URL + '/sendAudio?chat_id={}&audio={}&caption={}&parse_mode={}'
TELEGRAM_SEND_REPLY_MARKUP_URL = BASE_TELEGRAM_API_URL + '/sendMessage?chat_id={}&text={}&reply_markup={}'
TELEGRAM_SEND_TYPING_ACTION = BASE_TELEGRAM_API_URL + '/sendChatAction?chat_id={}&action={}'

msgs = {
    "/start": 'Olá! Sou o assistente da NOS!\n' +
        'Posso-te ajudar com informações sobre <b>cinemas</b>, <b>serviços da NOS</b> e <b>resolução de problemas técnicos</b>.\n' +
        'Para mais informações sobre mim utiliza o comando /help.\n' +
        'Caso desejes reiniciar a conversa utiliza o comando /reset.\n' +
        'Estou pronto para responder aos teus pedidos nesta conversa!\n\n' +
        'Em que te posso ser útil?',
    "/help": 'Este bot pode ser dividido em 3 categorias:\n' +
        '* <b>Cinemas</b>: permite a procura de cinemas perto de si, assim como a procura e a obtenção de informações sobre filmes e sessões, consoante variados critérios.\n' +
        '* <b>Serviços da NOS</b>: permite a procura de linhas de apoio, telemóveis para venda, tarifários WTF, pacotes da NOS (como satélite ou fibra), assim como a procura de lojas da NOS.\n' +
        '* <b>Resolução de problemas técnicos</b>: permite obter sugestões para resolver os problemas técnicos dos clientes da NOS.\n\n' +
        'Para além disto, o bot contém ainda um <b>modo interativo</b> que permite guiar o processo de obtenção de informações por parte do utilizador. Para entar neste modo basta utilizar o comando /interativo.',
    "inactive": 'Ainda te lembras de mim? Sou o assistente da NOS!\n' +
        'Posso-te ajudar com informações sobre <b>cinemas</b>, <b>serviços da NOS</b> e <b>resolução de problemas técnicos</b>.\n' +
        'Para mais informações sobre mim utiliza o comando /help.\n' +
        'Caso desejes reiniciar a conversa utiliza o comando /reset.\n' +
        'Estou pronto para responder aos teus pedidos nesta conversa!\n\n' +
        'Em que te posso ser útil?',
}

INACTIVE_TIME = 5 # minutes
NOTIFICATION_TASK_INTERVAL = 1 # minutes