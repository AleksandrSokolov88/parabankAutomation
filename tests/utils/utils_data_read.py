import yaml


# Data Transfer Object Pattern
class GetData:
    __data = ""

    # Get data of specific topic
    def get_data(self, path_to_file):
        with open(path_to_file, "r") as file:
            self.__data = yaml.safe_load(file)
        return self.__data
