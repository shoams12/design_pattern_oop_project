from States.state import State


class NormalState(State):


    def start(self):
        print("The game is already running!")

    def take_hit(self, damage):
        self._spaceship.take_damage(damage)
        self._state_change_check()

    def repair(self, points):
        self._spaceship.repair(points)
        self._state_change_check()

    def complete_level(self):
        if self._level == State.TOTAL_LEVELS:
            from game_over_win_state import GameOverWinState
            self._game.state = GameOverWinState(self._game, self._spaceship, self._level)
        else:
            self._level += 1

    def _state_change_check(self):
        from States.danger_state import DangerState
        from States.game_over_lose_state import GameOverLoseState

        if self._spaceship.is_destroyed():
            self._game.state = GameOverLoseState(self._game, self._spaceship, self._level)
        elif self._spaceship.points <= State.DANGER_LIMIT:
            self._game.state = DangerState(self._game, self._spaceship, self._level)