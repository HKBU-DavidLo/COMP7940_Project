from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import FlexSendMessage, TextSendMessage, TextMessage

import configparser

import re

config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))

def keyword_flex(event):
    #JSON from LINE SIMULATOR
    carousel_flex = {
        "type": "carousel",
        "contents": [{
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://images.unsplash.com/flagged/photo-1584036561584-b03c19da874c?ixlib=rb-1.2.1&auto=format&fit=crop&w=1489&q=80",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "COVID-19 News",
                    "weight": "bold",
                    "size": "md",
                    "color": "#FF0055"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [{
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [{
                            "type": "text",
                            "text": "BBC news",
                            "color": "#8f8f8f",
                            "size": "sm",
                            "flex": 5,
                            "margin": "md"
                        }]
                    }]
                }],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "Please click here",
                    "flex": 0,
                    "margin": "md",
                    "action": {
                        "type": "uri",
                        "label": "action",
                        "uri": "https://www.bbc.com/zhongwen/trad/topics/a3b15769-775e-471d-a511-a7b78f346859"
                    },
                    "color": "#1ABBAB"
                }]
            },
            "styles": {
                "body": {
                    "backgroundColor": "#FFD711"
                },
                "footer": {
                    "backgroundColor": "#FFD711"
                }
            }
        },
        {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://www.timeshighereducation.com/sites/default/files/styles/medium/public/hong_kong_baptists_logo.jpg?itok=--nQ3fBu",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "HKBU update",
                    "weight": "bold",
                    "size": "md",
                    "color": "#0DE39C"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [{
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [{
                            "type": "text",
                            "text": "COVID-19 arrangements",
                            "color": "#8c8c8c",
                            "size": "xs",
                            "flex": 5,
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": "http://ehsu.hkbu.edu.hk/2019-nCOV/"
                            }   
                        }]
                    }]
                }],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "Please click here",
                    "color": "#BB0FFB"
                }]
            },
            "styles": {
                "body": {
                    "backgroundColor": "#E6E6E6"
                },
                "footer": {
                    "backgroundColor": "#E6E6E6"
                }
            }
        },
        {
            "type": "bubble",
            "size": "micro",
            "hero": {
                "type": "image",
                "url": "https://www.chp.gov.hk/files/png/logo_dh_en.png",
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "COVID-19 FAQ",
                    "weight": "bold",
                    "size": "sm",
                    "color": "#8C02F2"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [{
                        "type": "box",
                        "layout": "baseline",
                        "spacing": "sm",
                        "contents": [{
                            "type": "text",
                            "text": "Something you should be aware",
                            "color": "#8c8c8c",
                            "size": "xs",
                            "flex": 5
                        }]
                    }]
                }],
                "spacing": "sm",
                "paddingAll": "13px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [{
                    "type": "text",
                    "text": "Please click here",
                    "color": "#2F71E8"
                }]
            },
            "styles": {
                "body": {
                    "backgroundColor": "#2FF4F1"
                },
                "footer": {
                    "backgroundColor": "#2FF4F1"
                }
            }
        }]
    }

    if re.match("information", event.message.text.lower()):
        
        try:
            message = FlexSendMessage(alt_text="Carousel Checklist", contents=carousel_flex)
            line_bot_api.reply_message(
                event.reply_token,
                message
            )

            return True
        except:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="can't read flex")
            )
            return True
    else:
        return False
