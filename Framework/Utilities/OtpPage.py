from selenium.webdriver.common.by import By


class OTP:
    def __init__(self, driver):
        self.driver= driver

    code = (By.NAME, "code")
    submit = (By.ID, "cvf-submit-otp-button")


    def Code(self):
        code = self.driver.find_element(*OTP.code).send_keys("123456")
        return code

    def Submit(self):
        submit= self.driver.find_element(*OTP.submit).click()
        return submit

