import time
from testUI.POM.main_page import MainPage
from data.data_UI import DataUI as Data
from testUI.config_driver import Driver


class Test1:
    # Loading POM
    main_page = MainPage()
    # Loading WebDriver
    driver = Driver().get_driver()

    main_page.click_register_button(driver)
    time.sleep(3)
    driver.quit()

