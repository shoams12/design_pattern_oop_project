from abc import ABC, abstractmethod
class State(ABC):

    DANGER_LIMIT = 20  # under/equal to 20 getting danger_state
    TOTAL_LEVELS = 3  # number of levels

    def __init__(self, game, spaceship, level):
        self._game = game
        self._spaceship = spaceship
        self._level = level


    @property
    def game(self):
        return self._game

    @property
    def spaceship(self):
        return self._spaceship

    @property
    def level(self):
        return self._level

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def take_hit(self, damage):
        pass

    @abstractmethod
    def repair(self, points):
        pass

    @abstractmethod
    def complete_level(self):
        pass