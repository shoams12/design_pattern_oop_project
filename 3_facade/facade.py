
from subsystems.start_subsystem import StartSubsystem
from subsystems.end_subsystem import EndSubsystem
from subsystems.increase_subsystem import IncreaseSubsystem
from subsystems.reduce_subsystem import ReduceSubsystem
from subsystems.right_subsystem import RightSubsystem
from subsystems.left_subsystem import LeftSubsystem
from subsystems.fuel_subsystem import FuelSubsystem
from subsystems.location_subsystem import LocationSubsystem


class Facade:


    def __init__(self):
        self._start = StartSubsystem()
        self._end = EndSubsystem()
        self._increase = IncreaseSubsystem()
        self._reduce = ReduceSubsystem()
        self._right = RightSubsystem()
        self._left = LeftSubsystem()
        self._fuel = FuelSubsystem()
        self._location = LocationSubsystem()

    def start_drive(self):
        print("\nstart_drive() ---- ")
        self._fuel.show_fuel()
        self._start.start()
        self._location.show_location()

    def end_drive(self):
        print("\nend_drive() ---- ")
        self._reduce.reduce()
        self._location.move(5)
        self._end.end()
        self._fuel.show_fuel()
        self._location.show_location()

    def increase_speed(self):
        print("\nincrease_speed() ---- ")
        self._increase.increase()
        self._fuel.use_fuel(5)
        self._location.move(10)

    def reduce_speed(self):
        print("\nreduce_speed() ---- ")
        self._reduce.reduce()
        self._fuel.use_fuel(1)
        self._location.move(5)

    def turn_right(self):
        print("\nturn_right() ---- ")
        self._reduce.reduce()
        self._right.right()
        self._location.turn_right()
        self._fuel.use_fuel(2)
        self._location.move(5)

    def turn_left(self):
        print("\nturn_left() ---- ")
        self._reduce.reduce()
        self._left.left()
        self._location.turn_left()
        self._fuel.use_fuel(2)
        self._location.move(5)

    def show_fuel(self):
        print("\nshow_fuel() ---- ")
        self._fuel.show_fuel()

    def show_location(self):
        print("\nshow_location() ---- ")
        self._location.show_location()