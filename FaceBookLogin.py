from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = Options()
options.add_experimental_option('detach', True)
ser_obj = Service("Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)
driver.get("https://en-gb.facebook.com/")
driver.find_element(By.XPATH, "//input[@type= 'text']").send_keys("ramsteyn420@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("Ramsteyn8$")
driver.find_element(By.NAME, "login").click()

