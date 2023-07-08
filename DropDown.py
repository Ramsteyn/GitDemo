from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

credentials = ["Firstname", "Surname", "Mail ID", "Password", "Date of Birth", "Month of Birth", "Born Year", "Gender"]
user_Details = []

for i in credentials:
   user_Details.append(input("Please enter the " + i))

#print(user_Details)



options = Options()
options.add_experimental_option('detach', True)
ser_obj = Service("Documents\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj, options=options)
driver.implicitly_wait(5)
driver.get("https://en-gb.facebook.com/")
driver.find_element(By.LINK_TEXT, "Create new account").click()
driver.find_element(By.CSS_SELECTOR,"input[name='firstname']").send_keys(user_Details[0])
driver.find_element(By.CSS_SELECTOR,"input[name='lastname']").send_keys(user_Details[1])
driver.find_element(By.CSS_SELECTOR,"input[name='reg_email__']").send_keys(user_Details[2])
driver.find_element(By.CSS_SELECTOR,"input[name='reg_email_confirmation__']").send_keys(user_Details[2])
driver.find_element(By.XPATH,"//input[@name='reg_passwd__']").send_keys(user_Details[3])
dod = driver.find_elements(By.XPATH, "//select[@name='birthday_day']/option")
dom = driver.find_elements(By.XPATH, "//select[@name='birthday_month']/option")
doy = driver.find_elements(By.XPATH, "//select[@name='birthday_year']/option")

for i in dod:
    if str(i.text) == user_Details[4]:
        i.click()
        break

for j in dom:
    if str(j.text) == user_Details[5]:
        j.click()
        break

for k in doy:
    if str(k.text) == user_Details[6]:
        k.click()
        break
if user_Details[7] == "Female":
    driver.find_element(By.XPATH, '//span[@data-name= "gender_wrapper"]/span[1]').click()

else:
    driver.find_element(By.XPATH, '//span[@data-name= "gender_wrapper"]/span[2]').click()

driver.find_element(By.XPATH,"//button[@name='websubmit']").click()



# drop = Select(driver.find_element(By.LINK_TEXT, "Create new account"))
# drop.select_by_index(0)