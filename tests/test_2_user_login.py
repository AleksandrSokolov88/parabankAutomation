import time
from pom.main_page import MainPage
from steps.usersteps import UserSteps
from pom.accounts_overview import AccountsOverview


class Test2UserLogin:
    def test_2_user_login(self, data,driver):

        # Create main_page instance
        main_page = MainPage(driver)

        # Create accounts_overview instance
        accounts_overview = AccountsOverview(driver)

        # Using step for registration
        user_steps = UserSteps(driver, data)
        user_steps.registration_user_and_log_out()

        # Enter Username
        main_page.enter_username(data["user_name"])

        # Enter Password
        main_page.enter_password(data["password"])

        # CLick Log in button
        main_page.click_login_button()
        time.sleep(2)
        # Assertion
        assert accounts_overview.is_accounts_overview_displayed()
