import faker
import yaml


class DataFaker:
    __FAKER_METHODS_NAME = {
        "zip_code": "zipcode",
        "address": "street_name"
    }
    __data = []

    def __init__(self, test_name, amount_of_test_data=1):
        with open(f"tests/data/data_{test_name}.yaml", "r", encoding="utf-8") as file:
            data_from_file = yaml.safe_load(file)
            keys_for_faker: dict = data_from_file[0]
            for _ in range(amount_of_test_data):
                temp_dict = {}
                for key in keys_for_faker.keys():
                    if key in self.__FAKER_METHODS_NAME:
                        key_faker = self.__FAKER_METHODS_NAME[key]
                        temp_dict[key] = getattr(faker.Faker(), key_faker)()
                    else:
                        temp_dict[key] = getattr(faker.Faker(), key)()
                self.__data.append(temp_dict)

    def get_data(self):
        return self.__data
