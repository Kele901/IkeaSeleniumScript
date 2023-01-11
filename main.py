from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


options = webdriver.ChromeOptions()

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver.get("https://www.ikea.com/gb/en")

time.sleep(2)

cookies_consent = driver.find_element(by=By.ID, value = "onetrust-accept-btn-handler")


cookies_consent.send_keys(Keys.ENTER)


search = driver.find_element(by=By.XPATH, value ="/html[1]/body[1]/header[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/input[1]")

search.send_keys("bathroom")
search.send_keys(Keys.ENTER)

#cheapest_price_chairs = driver.find_element(by=By.XPATH, value ="/html[1]/body[1]/main[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[2]/button[1]")


list_of_Images = driver.find_elements(by = By.TAG_NAME, value = "img")

i = 0
while i < len(list_of_Images):
    print (list_of_Images[i].get_attribute('src'))
    i = i + 1

time.sleep(15)