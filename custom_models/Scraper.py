import selenium
from selenium import webdriver
import os
import time

def scrapeDataset():

    URL = "https://smolandsd.maps.arcgis.com/apps/opsdashboard/index.html#/209dbb6e547643c5aeac83aa8b9de719"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    driver.get(URL)
    time.sleep(5)


    elements = driver.find_elements_by_tag_name('text')
    confirmed = elements[1].text.strip()
    discharged = elements[4].text.strip()
    hospitalised = elements[7].text.strip()
    death = elements[13].text.strip()
    
    driver.quit()
    return (confirmed, discharged, hospitalised, death)
