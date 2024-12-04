import time
from driver_creator import Driver
from pom.main_page import MainPage
from pom.register_page import RegisterPage


class Test1UserRegistration:
    def test_1_user_registration(self, data):
        # Create driver
        driver = Driver().get_driver()

        # Create main_page instance
        main_page = MainPage(driver)

        # Create register_page instance
        register_page = RegisterPage(driver)

        # Go to BASE_URL
        driver.get(Driver.BASE_URL)

        # Click register button
        main_page.click_register_button()

        # Enter First name
        register_page.enter_first_name(data["first_name"])

        # Enter Last name
        register_page.enter_last_name(data["last_name"])

        # Enter Address
        register_page.enter_address(data["address"])

        # Enter City
        register_page.enter_city(data["city"])

        # Enter State
        register_page.enter_state(data["state"])

        # Enter Zip code
        register_page.enter_zip_code(data["zip_code"])

        # Enter Phone
        register_page.enter_phone(data["phone_number"])

        # Enter SSN
        register_page.enter_ssn(data["ssn"])

        # Enter Username
        register_page.enter_username(data["user_name"])

        # Enter Password
        register_page.enter_password(data["password"])

        # Confirm Password
        register_page.enter_confirm(data["password"])
        # CLick Register Button
        register_page.click_register()
        time.sleep(2)
        # Assertion
        assert (register_page.get_value_registration_success() ==
                "Your account was created successfully. You are now logged in.")
        driver.quit()