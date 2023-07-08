import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#user_Details = ["Ram", "Mani", "rdsrdx49@gmail.com", "Testing123"]
class Credentials:

    def __init__(self, driver):
        self.driver = driver

    name = (By.ID, "ap_customer_name")
    email = (By.NAME, "email")
    password = (By.ID, "ap_password")
    rePassword = (By.ID, "ap_password_check")
    cont = (By.ID, "continue")
    clname = (By.XPATH, "//div[@class='a-alert-content'][normalize-space()='Wrong or Invalid email address or mobile phone number. Please correct and try again.']")



    def CredentialsName(self,list):
        self.list = list
        name = self.driver.find_element(*Credentials.name).send_keys(self.list["Firstname"] + " " + self.list["Lastname"])
        return name

    def CredentialsEmail(self, list):
        self.list = list
        email = self.driver.find_element(*Credentials.email).send_keys(self.list["MailID"])
        return email

    def CredentialsPass(self, list):
        self.list = list
        password = self.driver.find_element(*Credentials.password).send_keys(self.list["Password"])
        return password

    def CredentialsRePass(self, list):
        self.list = list
        repassword =self.driver.find_element(*Credentials.rePassword).send_keys(self.list["Password"])
        return repassword

    def CredentialsContinue(self):
        cont = self.driver.find_element(*Credentials.cont).click()
        #wait = WebDriverWait(self.driver, 5)
        #wait.until(expected_conditions.presence_of_element_located((Credentials.clname)))
        #tt = self.driver.find_element(By.XPATH, "//div[@class='a-alert-content'][normalize-space()='Wrong or Invalid email address or mobile phone number. Please correct and try again.']").text
        #self.driver.find_elemnent(*Credentials.clname)
        return #tt



