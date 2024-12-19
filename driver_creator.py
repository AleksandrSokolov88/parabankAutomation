from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import yaml
import os


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
        chromedriver_path = os.path.join(os.getcwd(), 'drivers', 'chromedriver.exe')
        #chromedriver_path = '/var/jenkins_home/workspace/Test/drivers/chromedriver'
        service = Service(chromedriver_path)
        self.__driver = webdriver.Chrome(service=service, options=options)

    def get_driver(self) -> webdriver.Chrome:
        return self.__driver
