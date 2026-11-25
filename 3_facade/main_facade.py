"""
Facade + Proxy Design Pattern - Car
"""
from facade import Facade
from proxy import Proxy


if __name__ == '__main__':
    print("===== Facade =====")
    facade = Facade()
    facade.start_drive()
    facade.increase_speed()
    facade.turn_right()
    facade.turn_left()
    facade.reduce_speed()
    facade.show_fuel()
    facade.show_location()
    facade.end_drive()

    print("\n===== Proxy =====")
    proxy = Proxy()
    proxy.show_fuel()
    proxy.show_location()


    # Wait for user
    input("\nPress Enter to exit...")