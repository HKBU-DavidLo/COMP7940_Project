from __future__ import unicode_literals
import os

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, LocationMessage, LocationSendMessage

import configparser

#import random

from custom_models import CallDatabase, utils

# get LINE tokens from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))


def defaul_reply(event):
    reply = "Sorry, no meaningful reply is available."
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply)
    )

def location_search(event):
    #Text Message should start from 'location of' and followed by the name of the hospital
    if 'location of' in event.message.text.lower():
        try:
            try:
                target = event.message.text[12:]
                lat, lon = CallDatabase.getcoordinates(target)
                location = LocationSendMessage(
                    title = target,
                    address = 'Hong Kong',
                    latitude = float(lat),
                    longitude = float(lon)
                )
                line_bot_api.reply_message(
                    event.reply_token, location
                )
            except:
                #reply Sanatorium & Hospital if fail
                lat = 22.269562
                lon = 114.1807733
                line_bot_api.reply_message(
                    event.reply_token,
                    LocationSendMessage(
                        'Hong Kong Sanatorium & Hospital',
                        'Hong Kong',
                        lat,
                        lon
                    )
                )
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Sorry, failed to get location.")
            )
        return True
    else:
        return False


def epicdemic_record(event):
    try:
        reply = utils.prepare_redis_record().decode('UTF-8')
        
    except:
        reply = str(event.message.text) + " : failed to access database"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= reply)
    )
    return True

def scrape_manual(event):
    scrape_success = utils.prepare_scrape()
    return epicdemic_record(event)


# initial input data to Redis
def setupRedis(event):
    try:
        reply = utils.setup_redis()
    except:
        reply = "Cannot set up redis"
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= reply)
    )
    return True

    
