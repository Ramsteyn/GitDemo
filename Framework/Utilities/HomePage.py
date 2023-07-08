from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.ID, "nav-link-accountList")

    def account(self):
         home = self.driver.find_element(*HomePage.shop).click()

         return home
