import time
from steps.usersteps import UserSteps
from pom.open_new_account import NewAccount
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test3OpenNewAccount:
    def test_3_open_new_account(self, data, driver):
        # Steps for registration and log in
        user_steps = UserSteps(driver, data)
        user_steps.registration_user_and_log_out()
        user_steps.log_in_user()

        # Create new_account instance
        new_account = NewAccount(driver)

        # Click on the new account in the left menu
        new_account.click_open_new_account_menu()

        # Click on the new account button
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(new_account.get_account_opened_title()))
        new_account.click_open_new_account_button()

        # Get Account Opened Title
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(new_account.get_account_opened_title()))
        account_opened_title = new_account.get_account_opened_text()

        # Assertion
        assert account_opened_title == "Account Opened!"
