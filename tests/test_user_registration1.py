import time
import pytest
from driver_creator import Driver
from pom.main_page import MainPage
from pom.register_page import RegisterPage


class Test1UserRegistration:
    def test1_user_registration(self, data):
        # Create driver
        print(f"Data received in test: {data}")
        driver = Driver().get_driver()

        # Create main_page instance
        main_page = MainPage()

        # Create register_page instance
        register_page = RegisterPage(driver)

        # Go to BASE_URL
        driver.get(Driver.BASE_URL)

        # Click register button
        main_page.click_register_button(driver)
        time.sleep(2)

        # Enter First name
        register_page.enter_first_name(data["first_name"])

        # Enter Last name
        register_page.enter_last_name(data["last_name"])

        # Enter address
        register_page.enter_address(data["address"])

        # Enter City
        register_page.enter_city(data["city"])

        # Enter State
        register_page.enter_state(data["state"])

        # Enter zip code
        register_page.enter_zip_code(data["zip_code"])

        # Enter Phone
        register_page.enter_phone(data["phone"])

        # Enter SSN
        register_page.enter_ssn(data["ssn"])

        # Enter username
        register_page.enter_username(data["username"])

        # Enter password
        register_page.enter_password(data["password"])

        # Confirm password
        register_page.enter_confirm(data["password"])
        time.sleep(4)
        driver.quit()
