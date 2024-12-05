from pom.register_page import RegisterPage
from pom.main_page import MainPage
import time


class UserSteps:
    def __init__(self, driver, data):
        self.register_page = RegisterPage(driver)
        self.main_page = MainPage(driver)
        self.data = data

    def registration_user_and_log_out(self):
        self.main_page.click_register_button()
        self.register_page.enter_first_name(self.data["first_name"])
        self.register_page.enter_last_name(self.data["last_name"])
        self.register_page.enter_address(self.data["address"])
        self.register_page.enter_city(self.data["city"])
        self.register_page.enter_state(self.data["state"])
        self.register_page.enter_zip_code(self.data["zip_code"])
        self.register_page.enter_phone(self.data["phone_number"])
        self.register_page.enter_ssn(self.data["ssn"])
        self.register_page.enter_username(self.data["user_name"])
        self.register_page.enter_password(self.data["password"])
        self.register_page.enter_confirm(self.data["password"])
        self.register_page.click_register()
        self.register_page.click_log_out_button()
        time.sleep(2)

    def log_in_user(self):
        self.main_page.enter_username(self.data["user_name"])
        self.main_page.enter_password(self.data["password"])
        self.main_page.click_login_button()
