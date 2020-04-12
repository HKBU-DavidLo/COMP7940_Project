import re
import random
import time

from custom_models import CallRedis, Scraper


def prepare_redis_record():    
    try:
        latest_rec_time = CallRedis.getLatestRecTime()
        SHORTEST_UPDATE_TIME = 28800 # 8 hours for avoiding frequent scraping
        # obtain value from Redis database
        confirmed = CallRedis.getHKCovidNum("Confirmed")
        discharged = CallRedis.getHKCovidNum("Discharged")
        hospital = CallRedis.getHKCovidNum("Hospitalised")
        death = CallRedis.getHKCovidNum("Death")
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
    CallRedis.update_redis_record("Confirmed", confirmed).decode('UTF-8')
    CallRedis.update_redis_record("Discharged", discharged).decode('UTF-8')
    CallRedis.update_redis_record("Hospitalised", hospital).decode('UTF-8')
    CallRedis.update_redis_record("Death", death).decode('UTF-8')
    return True    
        
def setup_redis():
    CallRedis.update_redis_record("Confirmed", 990)
    CallRedis.update_redis_record("Discharged", 309)
    CallRedis.update_redis_record("Hospitalised", 661)
    CallRedis.update_redis_record("Death", 4)
    reply = "Redis records added"
    return reply
