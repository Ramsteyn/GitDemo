from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# chrome service
from selenium.webdriver.chrome.service import Service
import time

# Enables to open the browser until close or quit func line is used
options = Options()
options.add_experimental_option('detach', True)
ser_obj = Service("Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)
driver.get("https://www.facebook.com/")
# maximize the window
driver.maximize_window()
#time.sleep(20)
print(driver.title)
print(driver.current_url)
driver.close()
