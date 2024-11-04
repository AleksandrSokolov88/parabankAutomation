from selenium.webdriver.support.select import By
from selenium import webdriver


class RegisterPage:

    def __init__(self, driver: webdriver.Chrome):
        self.__driver = driver

    __FIRST_NAME_FIELD = (By.XPATH, '//input[@id="customer.firstName"]')
    __LAST_NAME_FIELD = (By.XPATH, '//input[@id="customer.lastName"]')
    __ADDRESS = (By.XPATH, '//input[@id="customer.address.street"]')
    __CITY = (By.XPATH, '//input[@id="customer.address.city"]')
    __STATE = (By.XPATH, '//input[@id="customer.address.state"]')
    __ZIP_CODE = (By.XPATH, '//input[@id="customer.address.zipCode"]')
    __PHONE = (By.XPATH, '//input[@id="customer.phoneNumber"]')
    __SSN = (By.XPATH, '//input[@id="customer.ssn"]')
    __USERNAME = (By.XPATH, '//input[@id="customer.username"]')
    __PASSWORD = (By.XPATH, '//input[@id="customer.password"]')
    __CONFIRM = (By.XPATH, '//input[@id="repeatedPassword"]')

    def enter_first_name(self, value):
        self.__driver.find_element(*self.__FIRST_NAME_FIELD).send_keys(value)

    def enter_last_name(self, value):
        self.__driver.find_element(*self.__LAST_NAME_FIELD).send_keys(value)

    def enter_address(self, value):
        self.__driver.find_element(*self.__ADDRESS).send_keys(value)

    def enter_city(self, value):
        self.__driver.find_element(*self.__CITY).send_keys(value)

    def enter_state(self, value):
        self.__driver.find_element(*self.__STATE).send_keys(value)

    def enter_zip_code(self, value):
        self.__driver.find_element(*self.__ZIP_CODE).send_keys(value)

    def enter_phone(self, value):
        self.__driver.find_element(*self.__PHONE).send_keys(value)

    def enter_ssn(self, value):
        self.__driver.find_element(*self.__SSN).send_keys(value)

    def enter_username(self, value):
        self.__driver.find_element(*self.__USERNAME).send_keys(value)

    def enter_password(self, value):
        self.__driver.find_element(*self.__PASSWORD).send_keys(value)

    def enter_confirm(self, value):
        self.__driver.find_element(*self.__CONFIRM).send_keys(value)
