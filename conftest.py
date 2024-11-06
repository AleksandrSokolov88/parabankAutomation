import yaml
from tests.utils.utils_data_read import GetData
from tests.data.data_user_faker import DataFaker
from pytest import Metafunc


def pytest_generate_tests(metafunc: Metafunc):
    test_name = metafunc.definition.name
    with open("config/config_tests.yaml", "r") as file2:
        my_dict: dict = yaml.safe_load(file2)
    if test_name in my_dict.keys():
        if my_dict[test_name] == "Yaml":
            data = GetData().get_data("tests/data/data_user.yaml")
        elif "Faker" in my_dict[test_name]:
            quantity_of_test_data = my_dict[test_name].split()
            data = DataFaker(int(quantity_of_test_data[-1])).get_data_list()
    metafunc.parametrize("data", data)
