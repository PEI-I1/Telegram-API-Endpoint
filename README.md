# Telegram-API-Endpoint

## Usage
#### Development Setup

* Crete a Telegram Bot:
    * Using **BotFather** on Telegram create a bot using command `/newbot`.
    * Copy the bot token and paste it on *BOT_TOKEN* field in `config.py`.

* Using `ngrok` to forward requests to our `localhost`:
    * Download/Install `ngrok`.
    * Run `./ngrok http 5000`.
    * Copy the **https** link that appears on terminal and paste it on *NGROK_URL* field in `config.py`.

* Run the bot using:
`./app.py`

* Use the bot you created on Telegram application.