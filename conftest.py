import yaml
from tests.utils.utils_yaml_faker_data_getter import DataGetter
from tests.utils.data_generator_faker_test_1_user_registration import DataFaker
from tests.utils.data_generator_faker_test_2_user_login import DataFaker
from pytest import Metafunc


def pytest_generate_tests(metafunc: Metafunc):
    test_name = metafunc.definition.name
    with open("config/config_tests.yaml", "r", encoding="utf-8") as file:
        my_dict: dict = yaml.safe_load(file)
    if test_name in my_dict.keys():
        if my_dict[test_name] == "Yaml":
            prefix = "yaml"
        else:
            quantity_of_test_data = my_dict[test_name].split()
            DataFaker(int(quantity_of_test_data[-1])).write_data_to_file()
            prefix = "faker"
        data = DataGetter().get_data(f"tests/data/data_{prefix}_{test_name}.yaml")
    metafunc.parametrize("data", data)
