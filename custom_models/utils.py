import re
import random
import time

from custom_models import CallRedis, Scraper


def prepare_redis_record():    
    try:
        latest_rec_time = CallRedis.getLatestRecTime()
        SHORTEST_UPDATE_TIME = 28800 # 8 hours for avoiding frequent scraping
        # obtain value from Redis database
        confirmed = CallRedis.getHKCovidNum("Confirmed").decode('UTF-8')
        discharged = CallRedis.getHKCovidNum("Discharged").decode('UTF-8')
        hospital = CallRedis.getHKCovidNum("Hospitalised").decode('UTF-8')
        death = CallRedis.getHKCovidNum("Death").decode('UTF-8')
        scraped = False
        if (int(time.time()) - latest_rec_time > SHORTEST_UPDATE_TIME):
             #update values in Redis database if data is more than SHORTEST_UPDATE_TIME old
             scraped = prepare_scrape()

        reply = (f'According to latest information: '
                 f'no. of confirmed cases: {confirmed}. '
                 f'no. of discharged cases: {discharged}, '
                 f'no. of hospitalised cases: {hospital}, '
                 f'no. of death cases: {death}.'
        )
        if scraped:
            reply = reply + ' (page scraped)'
    except:
        reply = "Failed to obtain Redis database"
    return reply


def prepare_scrape():
    (confirmed, discharged, hospital, death) = Scraper.scrapeDataset()
    CallRedis.update_redis_record("Confirmed", confirmed)
    CallRedis.update_redis_record("Discharged", discharged)
    CallRedis.update_redis_record("Hospitalised", hospital)
    CallRedis.update_redis_record("Death", death)
    return True    
        
def setup_redis():
    CallRedis.update_redis_record("Confirmed", 990)
    CallRedis.update_redis_record("Discharged", 309)
    CallRedis.update_redis_record("Hospitalised", 661)
    CallRedis.update_redis_record("Death", 4)
    reply = "Redis records added"
    return reply
