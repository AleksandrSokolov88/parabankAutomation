from faker import Faker


class DataFaker:
    def __init__(self, data_sets=1):
        faker = Faker()
        self.__data_list = []
        self.__data_sets = data_sets
        for i in range(self.__data_sets):
            data_dict = {
                "first_name": faker.first_name(),
                "last_name": faker.last_name(),
                "address": faker.street_name(),
                "city": faker.city(),
                "state": faker.state(),
                "zip_code": faker.zipcode(),
                "phone": faker.phone_number(),
                "ssn": faker.ssn(),
                "username": faker.user_name(),
                "password": faker.password()
            }
            self.__data_list.append(data_dict)

    def get_data_list(self):
        return self.__data_list

