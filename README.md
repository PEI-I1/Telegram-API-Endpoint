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

## API

<details>
<summary>Get response for a user message</summary>

```http
POST /webhook
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `message.from.id` | `int` | **Required**. User id. |
| `message.from.first_name` | `string` | **Required**. User first name. |
| `message.from.last_name` | `string` | **Required**. User last name. |
| `message.chat.id` | `int` | **Required**. Chat id. |
| `message.text` | `string` | **Optional**. User message. |
| `message.date` | `int` | **Required**. Message Date in Unix time. |
| `location.latitude` | `float` | **Optional**. User latitude location. |
| `location.longitude` | `float` | **Optional**. User longitude location. |

Example:
```
{
    'message': {
        'from': {
            'id': 912544244,
            'first_name': 'António',
            'last_name': 'Faria'
        },
        'chat': {
            'id': 912544244
        },
        'text': 'cinemas',
        'date': 1579519622
    }
}
```

Example with location:
```
{
    'message': {
        'from': {
            'id': 912544244,
            'first_name': 'António',
            'last_name': 'Faria'
        },
        'chat': {
            'id': 912544244
        },
        'location': {
            'latitude': 33.542111,
            'longitude': -10.444713
        },
        'date': 1579519622
    }
}
```

Send the necessary content to `CHAT_PROCESSOR_URL + "/getResponse"`

------
</details>

<details>
<summary>Send a message to user</summary>

```http
POST /send_message/<string:idChat>
```

The `body` should have the messsage encoded in 'UTF-8'.

Will show a message in Telegram user chat.

------
</details>

<details>
<summary>Send a silent message to user</summary>

```http
POST /send_silent_message/<string:idChat>
```

The `body` should have the messsage encoded in 'UTF-8'.

Will show a silent message in Telegram user chat.

------
</details>

<details>
<summary>Send a photo to user</summary>

```http
POST /send_photo/<string:idChat>
```

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `photo` | `string` | **Required**. Photo URL. |
| `caption` | `string` | **Required**. Photo caption. |

Example:
```
{
    'photo': 'http://cinemas.nos.pt/_layouts/15/Handlers/RenderImage.ashx?file=52278.jpg',
    'caption': '<b>Título: </b>Mulan\n<b>Elenco: </b>Yifei Liu, Donnie Yen, Jason Scott Lee\n<b>Género: </b>Aventura\n'
}
```

Will show a photo with a caption in Telegram user chat.

------
</details>

<details>
<summary>Request user location</summary>

```http
GET /get_location/<string:idChat>
```

Will show a button in Telegram user chat for user send his/her GPS location.

------
</details>
