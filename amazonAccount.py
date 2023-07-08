from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

credentials = ["Firstname", "Surname", "Mail ID", "Password"]
user_Details = []

for i in credentials:
   user_Details.append(input("Please enter the " + i))
#print(user_Details)

i = 0


options = Options()
options.add_experimental_option('detach', True)
ser_obj = Service("Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://www.amazon.com/")
driver.find_element(By.ID, "nav-link-accountList").click()
#driver.find_element(By.LINK_TEXT, "Add account").click()
driver.find_element(By.LINK_TEXT, "Create your Amazon account").click()
driver.find_element(By.ID, "ap_customer_name").send_keys(user_Details[0]+" "+user_Details[1])
driver.find_element(By.NAME, "email").send_keys(user_Details[2])
driver.find_element(By.ID, "ap_password").send_keys(user_Details[3])
driver.find_element(By.ID, "ap_password_check").send_keys(user_Details[3])
driver.find_element(By.ID, "continue").click()
wait = WebDriverWait(driver, 10)

t = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='a-alert-content'][normalize-space()='Wrong or Invalid email address or mobile phone number. Please correct and try again.']")))
tt = driver.find_element(By.XPATH, "//div[@class='a-alert-content'][normalize-space()='Wrong or Invalid email address or mobile phone number. Please correct and try again.']").text
print(f"{tt}")
#driver.find_element(By.NAME, "code").send_keys(input(i))
#driver.find_element(By.ID, "cvf-submit-otp-button").click()

