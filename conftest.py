import pytest
import yaml
from tests.utils.data_getter_yaml import DataGetter
from tests.utils.data_generator_faker import DataFaker
from pytest import Metafunc
from tests.utils.parabank_database import Database
from driver_creator import Driver
from pytest import Item
from pytest import CallInfo
import allure
import os
import shutil


def pytest_generate_tests(metafunc: Metafunc):
    test_case_name = metafunc.definition.name
    with open("config/config_tests.yaml", "r", encoding="utf-8") as file:
        test_cases_names: dict = yaml.safe_load(file)
    if test_case_name in test_cases_names.keys():
        if test_cases_names[test_case_name] == "Yaml":
            data = DataGetter().get_data(f"tests/data/data_{test_case_name}.yaml")
        else:
            amount_of_test_data: str = test_cases_names[test_case_name]
            data = DataFaker(test_case_name, int(amount_of_test_data[-1])).get_data()
    metafunc.parametrize("data", data)


@pytest.fixture(scope="session", autouse=True)
def clear_allure_folder():
    if os.path.exists("allure-results"):
        shutil.rmtree("allure-results")
    os.mkdir("allure-results")


@pytest.fixture(scope="class", autouse=True)
def setup_database():
    Database.start_database()
    yield
    Database.clear_database()


@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = Driver().get_driver()
    driver.get(Driver.BASE_URL)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    outcome = yield
    result: pytest.TestReport = outcome.get_result()
    if result.outcome == "failed":
        driver = item.funcargs['driver']
        screenshot_name = "screenshot_error.jpg"
        driver.save_screenshot(screenshot_name)
        with open(screenshot_name, "rb") as file:
            allure.attach(file.read(), attachment_type=allure.attachment_type.JPG)
        os.remove(screenshot_name)
