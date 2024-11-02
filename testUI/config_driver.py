from selenium import webdriver
from data.data_UI import DataUI


class Driver:
    __driver = None

    def __init__(self):
        self.__driver = webdriver.Chrome()
        self.__driver.get(DataUI.BASE_URL)

    def get_driver(self):
        return self.__driver
