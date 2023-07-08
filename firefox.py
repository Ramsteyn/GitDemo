from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Enables to open the browser until close or quit func line is used
options = Options()
ser_obj = Service("Documents\\geckodriver.exe")
driver = webdriver.Firefox(service=ser_obj, options=options)
driver.get("https://www.facebook.com/")
# maximize the window
driver.maximize_window()
#time.sleep(20)
print(driver.title)
print(driver.current_url)
# driver.close()
