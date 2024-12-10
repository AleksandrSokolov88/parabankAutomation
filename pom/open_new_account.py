from selenium import webdriver
from selenium.webdriver.common.by import By


class NewAccount:
    def __init__(self, driver: webdriver.Chrome):
        self.__driver = driver

    __OPEN_NEW_ACCOUNT_MENU = (By.XPATH, '//a[text()="Open New Account"]')
    __OPEN_NEW_ACCOUNT_BUTTON = (By.XPATH, '//input[@value="Open New Account"]')
    __ACCOUNT_OPENED_TITLE = (By.XPATH, '//div[@id="openAccountResult"]//h1')
    __EXISTING_ACCOUNT = (By.XPATH, '//select[@id="fromAccountId"]')

    def click_open_new_account_menu(self):
        self.__driver.find_element(*self.__OPEN_NEW_ACCOUNT_MENU).click()

    def click_open_new_account_button(self):
        self.__driver.find_element(*self.__OPEN_NEW_ACCOUNT_BUTTON).click()

    def get_account_opened_text(self):
        return self.__driver.find_element(*self.__ACCOUNT_OPENED_TITLE).text

    def get_open_new_account_button(self):
        return self.__OPEN_NEW_ACCOUNT_BUTTON

    def get_account_opened_title(self):
        return self.__ACCOUNT_OPENED_TITLE

    def get_existing_account(self):
        return self.__EXISTING_ACCOUNT
