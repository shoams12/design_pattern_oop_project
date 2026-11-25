from spaceship import Spaceship
from States.new_game_state import NewGameState
import time

class Game:
    def __init__(self, player, spaceship_name):
        # New games start in 'NewGameState' by default
        self._player = player
        self._spaceship = Spaceship(spaceship_name)
        self._state = NewGameState(self, self._spaceship)

    @property
    def spaceship(self):
        return self._spaceship

    @property
    def hit_points(self):
        return self._spaceship.points

    @property
    def level(self):
        return self._state.level

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value

    def start(self):
        self._state.start()
        self._print_status("Start")

    def take_hit(self, damage):
        self._state.take_hit(damage)
        self._print_status(f"Took hit of {damage} 💥")

    def repair(self, points):
        self._state.repair(points)
        self._print_status(f"Repaired {points}")

    def complete_level(self):
        self._state.complete_level()
        self._print_status("Level completed")

    def _print_status(self, action):
        print(f"{action} --- ")
        print(f" 🚀 Hit points = {self.hit_points}")
        print(f" Level      = {self.level}")
        print(f" Status     = {type(self._state).__name__}")
        time.sleep(3)
        print()