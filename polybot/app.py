import flask
from flask import request
import os
from bot import Bot, QuoteBot, ImageProcessingBot
from img_proc import Img

app = flask.Flask(__name__)

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    BOT.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    #BOT = QuoteBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)
    BOT = ImageProcessingBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)

  #  my_img = Img('/home/shantalberkhof/PycharmProjects/ImageProcessingService/.img/colorpixels.png')
  #  my_img.blur()
   # my_img.save_img()

    app.run(host='0.0.0.0', port=8443)

