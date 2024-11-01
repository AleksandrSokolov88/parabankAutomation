from selenium import webdriver

driver = webdriver.Chrome()


class MainPage:
    USERNAME_FIELD = '//input[@type="text"]'
    PASSWORD_FIELD = '//input[@type="password"]'

    def enter_login(self, driver, value):
        driver = webdriver.Chrome()
        driver.find_element().send_keys(value)
