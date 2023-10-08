from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd
import time
import os
import sys

web = "https://bumble.com/app"
path = r"C:\Users\adity\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

options = Options()
options.headless=True
options.add_experimental_option("debuggerAddress", "localhost:9222")

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,options=options)

driver.get(web)
wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
numberOfLikes = 1

for i in range(numberOfLikes):
    try:
        likeButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@class='encounters-action__icon']/span[@class='icon icon--size-stretch'])[3]"))
        )
        likeButton.click()
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        

driver.quit()

#(//div[@class='encounters-action__icon']/span[@class='icon icon--size-stretch'])[3]