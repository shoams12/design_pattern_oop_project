from facade import Facade


class Proxy:

    def __init__(self):
        self.__facade = Facade()

    def show_fuel(self):
        self.__facade.show_fuel()

    def show_location(self):
        self.__facade.show_location()