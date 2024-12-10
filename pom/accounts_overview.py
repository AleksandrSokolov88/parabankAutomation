from selenium.webdriver.common.by import By
from selenium import webdriver


class AccountsOverview:

    def __init__(self, driver: webdriver.Chrome):
        self.__driver = driver

    __ACCOUNTS_OVERVIEW_TITLE = (By.XPATH, '//h1[contains(text(),"Accounts Overview")]')
    __ACCOUNT_NUMBER = (By.XPATH, '//td/a')

    def is_accounts_overview_displayed(self):
        return self.__driver.find_element(*self.__ACCOUNTS_OVERVIEW_TITLE).is_displayed()

    def get_account_number_text(self):
        return self.__driver.find_element(*self.__ACCOUNT_NUMBER).text

    def get_account_number_element(self):
        return self.__ACCOUNT_NUMBER
