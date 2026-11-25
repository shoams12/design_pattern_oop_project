
class FuelSubsystem:


    TANK_SIZE = 50  # liters

    def __init__(self):
        self._fuel = 35  # liters

    def show_fuel(self):
        percent = self._fuel / FuelSubsystem.TANK_SIZE * 100
        print(f"FuelSubsystem: {self._fuel} liters ({percent:.0f}%)")
        if self._fuel < 10:
             print("FuelSubsystem: Warning! Low fuel")

    def use_fuel(self, liters):
        self._fuel = max(0, self._fuel - liters)