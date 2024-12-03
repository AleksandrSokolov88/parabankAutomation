from faker import Faker


class DataFaker:
    def __init__(self, data_sets=1):
        faker = Faker()
        self.__data_list = []
        self.__data_sets = data_sets
        for i in range(self.__data_sets):
            data_dict = {
                "username": faker.user_name(),
                "password": faker.password()
            }
            self.__data_list.append(data_dict)

    def write_data_to_file(self):
        with open("tests/data/data_faker_test_2_user_login.yaml", "w") as file:
            file.write(str(self.__data_list))
