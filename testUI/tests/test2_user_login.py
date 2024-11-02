import time
from testUI.POM.main_page import MainPage
from data.data_UI import DataUI as Data
from testUI.config_driver import Driver


class Test2:  # Log in as a user
    # Loading POM
    main_page = MainPage()
    # Loading WebDriver
    driver = Driver().get_driver()

    main_page.start_page(driver, Data.BASE_URL)
    main_page.enter_login(driver, Data.USERNAME)
    main_page.enter_password(driver, Data.PASSWORD)
    main_page.click_login_button(driver)
    time.sleep(2)
    driver.quit()
