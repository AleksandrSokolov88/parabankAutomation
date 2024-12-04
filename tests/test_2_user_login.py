import time
from driver_creator import Driver
from pom.main_page import MainPage
from steps.user_steps import User_steps
from pom.accounts_overview import Accounts_overview


class Test2UserLogin:
    def test_2_user_login(self, data):
        # Create driver
        driver = Driver().get_driver()

        # Create main_page instance
        main_page = MainPage(driver)

        # Create accounts_overview instance
        accounts_overview = Accounts_overview(driver)

        # Go to BASE_URL
        driver.get(Driver.BASE_URL)

        # Click register button
        main_page.click_register_button()

        # Using step for registration
        User_steps.registration_user_and_log_out(driver, data)

        # Enter Username
        main_page.enter_username(data["user_name"])

        # Enter Password
        main_page.enter_password(data["password"])

        # CLick Log in button
        main_page.click_login_button()
        time.sleep(2)
        # Assertion
        assert accounts_overview.is_accounts_overview_displayed() == True
        driver.quit()
