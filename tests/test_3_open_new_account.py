from steps.usersteps import UserSteps
from pom.open_new_account import NewAccount
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pom.accounts_overview import AccountsOverview


class Test3OpenNewAccount:
    def test_3_open_new_account(self, data, driver):
        # Create new_account instance
        new_account = NewAccount(driver)

        # Create accounts_overview instance
        accounts_overview = AccountsOverview(driver)

        # Steps for registration and log in
        user_steps = UserSteps(driver, data)
        user_steps.registration_user_and_log_out()
        user_steps.log_in_user()

        # Waiting for element to be visible
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(accounts_overview.get_account_number_element()))
        # Getting account number
        account_number = accounts_overview.get_account_number_text()

        # Click on the new account in the left menu
        new_account.click_open_new_account_menu()

        # Waiting for account number presents on the page
        WebDriverWait(driver, 10).until(
            expected_conditions.text_to_be_present_in_element(new_account.get_existing_account(), account_number))

        # Click on the new account button
        new_account.click_open_new_account_button()

        # Waiting for element to be visible
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(new_account.get_account_opened_title()))

        # Get Account Opened Title
        account_opened_title = new_account.get_account_opened_text()

        # Assertion
        assert account_opened_title == "Account Opened!"
