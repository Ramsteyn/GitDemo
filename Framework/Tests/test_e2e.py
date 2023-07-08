import pytest

from Framework.Test_Data.CredentialsData import credentialsData
from Framework.Utilities.BaseClass import baseClass
from selenium.webdriver.common.by import By

from Framework.Utilities.CredentialsPage import Credentials
from Framework.Utilities.HomePage import HomePage
from Framework.Utilities.NewAccountClick import ClickNNew
from Framework.Utilities.OtpPage import OTP


#credentials = ["Firstname", "Surname", "Mail ID", "Password"]
#user_Details = ["Ram", "Mani", "rdsrdx49@gmail.com", "Testing123"]



#@pytest.mark.usefixtures("setup")
class TestExample(baseClass):
    def test_first(self, setup,test_inputs_key):
        log = self.getLogger()
        self.driver.implicitly_wait(5)

        # HomePage Class
        log.info("Enter the Homepage")
        homePage = HomePage(self.driver)
        homePage.account()#.click()

        log.info("Clicking thr Sign in button")
        # driver.find_element(By.LINK_TEXT, "Add account").click()
        # NewAccount Button Clicking Page
        clickPage = ClickNNew(self.driver)
        clickPage.clickNCreate()#.click()

        log.info("Enter the Credentials")
        # Credentials Page and Inputs
        cred = Credentials(self.driver)
        cred.CredentialsName(test_inputs_key)#.send_keys(user_Details[0] + " " + user_Details[1])
        cred.CredentialsEmail(test_inputs_key)#.send_keys(user_Details[2])

        cred.CredentialsPass(test_inputs_key)#.send_keys(user_Details[3])
        cred.CredentialsRePass(test_inputs_key)#.send_keys(user_Details[3])
        t = cred.CredentialsContinue()#.click()
        #print(t)
        assert t == None,  f"Error is {t}"
        log.info("Validating the OTP")
        # OTP Validations
        otp = OTP(self.driver)
        otp.Code()#.send_keys("123456")
        otp.Submit()#.click()
        self.driver.get("https://www.amazon.com/")


    @pytest.fixture(params= credentialsData.cred("TC1"))
    def test_inputs(self, request):
        return request.param

    @pytest.fixture(params= credentialsData.cred("TC1"))#[{"Firstname":"Ram","Lastname":"Mani", "Mail":"rdsrdx49@gmail.com", "Password":"Testing123"}])
    def test_inputs_key(self, request):
        return request.param
        #self.driver.find_element(By.ID, "ap_customer_name").send_keys(user_Details[0] + " " + user_Details[1])
        #self.driver.find_element(By.NAME, "email").send_keys(user_Details[2])
        #self.driver.find_element(By.ID, "ap_password").send_keys(user_Details[3])
        #self.driver.find_element(By.ID, "ap_password_check").send_keys(user_Details[3])
        #self.driver.find_element(By.ID, "continue").click()
        #self.driver.find_element(By.NAME, "code").send_keys("123456")
        #self.driver.find_element(By.ID, "cvf-submit-otp-button").click()
