import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# file reading into a List
with open('automation+ubiquity.txt', 'r') as reader:
    con = reader.readlines()
# Automation
options = Options()
options.add_experimental_option('detach', True)
ser_obj = Service("Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)
driver.maximize_window()
d = ActionChains(driver)
driver.implicitly_wait(5)
driver.get("https://devicetracker.amazon.com/")
driver.find_element(By.ID, "user_name_field").send_keys("USERID")
driver.find_element(By.ID, "user_name_btn").click()
driver.find_element(By.ID, "password_field").send_keys("MID-WAYPIN")
time.sleep(15)
v = driver.find_element(By.LINK_TEXT, "Storage")
d.move_to_element(v).perform()
driver.find_element(By.LINK_TEXT, "Scan to Storage").click()
sel = Select(driver.find_element(By.ID, "scan_operation"))
sel.select_by_index(2)
rec = Select(driver.find_element(By.ID, "location_id"))
rec.select_by_value("515226")
driver.find_element(By.ID, "addAssetTag").click()



for j in con:
    driver.find_element(By.ID, "dsnInput").send_keys(j)
    driver.find_element(By.ID, "assetTagInput").send_keys("AHP")
    driver.find_element(By.ID, "assetTagInput").send_keys(Keys.ENTER)








