from pom.register_page import RegisterPage
from driver_creator import Driver
import yaml
import time


class User_steps:
    @classmethod
    def registration_user_and_log_out(cls, driver, data):
        register_page = RegisterPage(driver)
        register_page.enter_first_name(data["first_name"])
        register_page.enter_last_name(data["last_name"])
        register_page.enter_address(data["address"])
        register_page.enter_city(data["city"])
        register_page.enter_state(data["state"])
        register_page.enter_zip_code(data["zip_code"])
        register_page.enter_phone(data["phone_number"])
        register_page.enter_ssn(data["ssn"])
        register_page.enter_username(data["user_name"])
        register_page.enter_password(data["password"])
        register_page.enter_confirm(data["password"])
        register_page.click_register()
        register_page.click_log_out_button()
        time.sleep(2)
