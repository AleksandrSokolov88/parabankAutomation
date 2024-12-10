import allure
from selenium.webdriver.support.select import By
from selenium import webdriver


class RegisterPage:

    def __init__(self, driver: webdriver.Chrome):
        self.__driver = driver

    __FIRST_NAME_FIELD = (By.XPATH, '//input[@id="customer.firstName"]')
    __LAST_NAME_FIELD = (By.XPATH, '//input[@id="customer.lastName"]')
    __ADDRESS_FIELD = (By.XPATH, '//input[@id="customer.address.street"]')
    __CITY_FIELD = (By.XPATH, '//input[@id="customer.address.city"]')
    __STATE_FIELD = (By.XPATH, '//input[@id="customer.address.state"]')
    __ZIP_CODE_FIELD = (By.XPATH, '//input[@id="customer.address.zipCode"]')
    __PHONE_FIELD = (By.XPATH, '//input[@id="customer.phoneNumber"]')
    __SSN_FIELD = (By.XPATH, '//input[@id="customer.ssn"]')
    __USERNAME_FIELD = (By.XPATH, '//input[@id="customer.username"]')
    __PASSWORD_FIELD = (By.XPATH, '//input[@id="customer.password"]')
    __CONFIRM_FIELD = (By.XPATH, '//input[@id="repeatedPassword"]')
    __REGISTER_BUTTON = (By.XPATH, '//input[@value="Register"]')
    __REGISTRATION_SUCCESS = (By.XPATH, '//div[@id="rightPanel"]/p')
    __LOG_OUT_BUTTON = (By.XPATH, '//a[text()="Log Out"]')

    @allure.step("enter first name")
    def enter_first_name(self, value):
        self.__driver.find_element(*self.__FIRST_NAME_FIELD).send_keys(value)

    @allure.step("enter last name")
    def enter_last_name(self, value):
        self.__driver.find_element(*self.__LAST_NAME_FIELD).send_keys(value)

    def enter_address(self, value):
        self.__driver.find_element(*self.__ADDRESS_FIELD).send_keys(value)

    def enter_city(self, value):
        self.__driver.find_element(*self.__CITY_FIELD).send_keys(value)

    def enter_state(self, value):
        self.__driver.find_element(*self.__STATE_FIELD).send_keys(value)

    def enter_zip_code(self, value):
        self.__driver.find_element(*self.__ZIP_CODE_FIELD).send_keys(value)

    def enter_phone(self, value):
        self.__driver.find_element(*self.__PHONE_FIELD).send_keys(value)

    def enter_ssn(self, value):
        self.__driver.find_element(*self.__SSN_FIELD).send_keys(value)

    def enter_username(self, value):
        self.__driver.find_element(*self.__USERNAME_FIELD).send_keys(value)

    def enter_password(self, value):
        self.__driver.find_element(*self.__PASSWORD_FIELD).send_keys(value)

    def enter_confirm(self, value):
        self.__driver.find_element(*self.__CONFIRM_FIELD).send_keys(value)

    def click_register(self):
        self.__driver.find_element(*self.__REGISTER_BUTTON).click()

    def get_value_registration_success(self):
        return self.__driver.find_element(*self.__REGISTRATION_SUCCESS).text

    def click_log_out_button(self):
        self.__driver.find_element(*self.__LOG_OUT_BUTTON).click()
