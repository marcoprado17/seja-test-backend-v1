from flask import Flask, request
import telegram
import os
from dotenv import load_dotenv

load_dotenv()

global bot
bot = telegram.Bot(token=os.environ['TELEGRAM_TOKEN'])

app = Flask(__name__)

def get_response(text):
    return 'Hello World!'

@app.route('/{}'.format(os.environ['TELEGRAM_TOKEN']), methods=['POST'])
async def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    text = update.message.text.encode('utf-8').decode()

    response = get_response(text)
    async with bot:
        await bot.send_message(text=response, chat_id=chat_id)

    return 'ok'

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(threaded=True)
