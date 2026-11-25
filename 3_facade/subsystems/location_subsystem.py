
class LocationSubsystem:
    """
    The 'Subsystem' class
    """

    DIRECTIONS = ["North", "East", "South", "West"]

    def __init__(self):
        self._x = 0
        self._y = 0
        self._direction = 0  # 0 = North

    def show_location(self):
        direction = LocationSubsystem.DIRECTIONS[self._direction]
        print(f" LocationSubsystem: ({self._x}, {self._y}), facing {direction}")

    def turn_right(self):
        self._direction = (self._direction + 1) % 4

    def turn_left(self):
        self._direction = (self._direction - 1) % 4

    def move(self, distance):
        if self._direction == 0:    # North
            self._y += distance
        elif self._direction == 1:  # East
            self._x += distance
        elif self._direction == 2:  # South
            self._y -= distance
        else:                       # West
            self._x -= distance