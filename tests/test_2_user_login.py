import time

from driver_creator import Driver
from pom.main_page import MainPage


class Test2UserLogin:
    def test_2_user_login(self, data):
        # Create driver
        driver = Driver().get_driver()

        # Create main_page instance
        main_page = MainPage(driver)

        # Go to BASE_URL
        driver.get(Driver.BASE_URL)

        # Enter Username
        main_page.enter_username(data["username"])

        # Enter Password
        main_page.enter_password(data["password"])
        time.sleep(2)
