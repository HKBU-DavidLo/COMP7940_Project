from __future__ import unicode_literals

import redis
import datetime
import time
import os

r = redis.from_url(os.environ.get("REDIS_URL"))

def getLatestRecTime():

    keyLastUpdate = "last update"
    #input if not exist, interested in number of whole seconds only
    r.setnx (keyLastUpdate, int(time.time()))

    return int(r.get(keyLastUpdate))

def getHKCovidNum(key):
    return r.get(key)
    

def update_redis_record(key, value):
    r.set(key, value)
    r.set("last update", int(time.time()))
