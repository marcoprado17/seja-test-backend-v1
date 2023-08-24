from dotenv import load_dotenv

load_dotenv()

from flask import Flask, request
import telegram
import os
from utils import get_response
import json
import requests

global bot
bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])

app = Flask(__name__)

def send_message(text, chat_id):
  url = "https://api.telegram.org/bot{}/sendMessage".format(os.environ['TELEGRAM_TOKEN'])

  payload = json.dumps({
    "chat_id": chat_id,
    "text": text
  })
  headers = {
    'Content-Type': 'application/json'
  }

  requests.request("POST", url, headers=headers, data=payload)

@app.route('/{}'.format(os.environ['TELEGRAM_TOKEN']), methods=['POST'])
async def respond():
    
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()

    print('Telegram request received')
    print('chat_id: {}'.format(chat_id))
    print('msg_id: {}'.format(msg_id))
    print('text: {}'.format(text))

    response = get_response(text, chat_id)
    send_message(text=response, chat_id=chat_id)

    print('Telegram response sent')
    print('response: {}'.format(response))

    return 'ok'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(threaded=False)
