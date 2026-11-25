from States.state import State
import time

class GameOverLoseState(State):


    def start(self):
        from States.new_game_state import NewGameState
        self._game.state = NewGameState(self._game, self._spaceship)
        self._game.state.start()

    def take_hit(self, damage):
        print("Game over - you lost!")
        time.sleep(3)

    def repair(self, points):
        print("Game over - you lost!")
        time.sleep(3)

    def complete_level(self):
        print("Game over - you lost!")
        time.sleep(3)