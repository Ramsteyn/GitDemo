from selenium.webdriver.common.by import By


class ClickNNew:
    createButton = (By.LINK_TEXT, "Create your Amazon account")

    def __init__(self,driver):
        self.driver = driver

    def clickNCreate(self):
         click = self.driver.find_element(*ClickNNew.createButton).click()

         return click