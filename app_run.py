from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser

from custom_models import ChannelTalks, ChannelFlex #, utils

app = Flask(__name__)

# get LINE tokens from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# Obtain LINE information
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# repeat text message
@handler.add(MessageEvent, message=TextMessage)
# list out all reply options:
def reply_text_message(event):
    if event.source.user_id != "Udeadbeefdfeadfsdlkfdasofjewa":
        reply = False #not yet replied

        #trying reply by condition:
        if not reply:
            reply = ChannelTalks.location_search(event)
        if not reply:
            reply = ChannelFlex.keyword_flex(event)
        #***
        #To add other reply options
        #***
        #finally, if not get replied yet:
        if not reply:
            reply = ChannelTalks.echo(event)


if __name__ == "__main__":
    app.run()
