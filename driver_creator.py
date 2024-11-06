from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import yaml


# Add annotation for driver
# Figure out the absolute paths


class Driver:
    __driver = None
    BASE_URL = "https://parabank.parasoft.com/parabank"

    def __init__(self):
        options = Options()
        with open("config/config_driver.yaml", "r") as file:
            data = yaml.safe_load(file)
        if data:
            for i in data.split():
                options.add_argument(i)
        self.__driver = webdriver.Chrome(options=options)

    def get_driver(self) -> webdriver.Chrome:
        return self.__driver
