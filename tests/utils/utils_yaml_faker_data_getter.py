import yaml


# Data Transfer Object Pattern
class DataGetter:
    __data = ""

    # Get data of specific topic
    def get_data(self, path_to_file):
        if "yaml" in path_to_file:
            with open(path_to_file, "r") as file:
                self.__data = yaml.safe_load(file)
            return self.__data
        else:
            with open(path_to_file, "r") as file:
                self.__data = file.read()
            return self.__data
