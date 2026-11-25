from States.state import State
import time

class NewGameState(State):

    def __init__(self, game, spaceship):
        super().__init__(game, spaceship, 0)

    def start(self):
        from States.normal_state import NormalState
        self._spaceship.reset()
        print("The game has started! Good luck.")
        time.sleep(3)
        self._game.state = NormalState(self._game, self._spaceship, 1)

    def take_hit(self, damage):
        print("The game has not started yet!")
        time.sleep(3)

    def repair(self, points):
        print("The game has not started yet!")
        time.sleep(3)

    def complete_level(self):
        print("The game has not started yet!")
        time.sleep(3)