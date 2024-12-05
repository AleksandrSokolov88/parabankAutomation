from selenium.webdriver.common.by import By
from selenium import webdriver


class AccountsOverview:

    def __init__(self, driver: webdriver.Chrome):
        self.__driver = driver

    __ACCOUNTS_OVERVIEW_TITLE = (By.XPATH, '//h1[contains(text(),"Accounts Overview")]')

    def is_accounts_overview_displayed(self):
        return self.__driver.find_element(*self.__ACCOUNTS_OVERVIEW_TITLE).is_displayed()
