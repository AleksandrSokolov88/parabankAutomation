from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:
    __USERNAME_FIELD = (By.XPATH, '//input[@type="text"]')
    __PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    __LOG_IN_BUTTON = (By.XPATH, '//input[@type="submit"]')
    __REGISTER_BUTTON = (By.XPATH, '//a[text()="Register"]')

    def enter_login(self, driver: webdriver.Chrome, value: str):
        driver.find_element(*self.__USERNAME_FIELD).send_keys(value)

    def enter_password(self, driver: webdriver.Chrome, value: str):
        driver.find_element(*self.__PASSWORD_FIELD).send_keys(value)

    def click_login_button(self, driver: webdriver.Chrome):
        driver.find_element(*self.__LOG_IN_BUTTON).click()

    def click_register_button(self, driver: webdriver.Chrome):
        driver.find_element(*self.__REGISTER_BUTTON).click()
