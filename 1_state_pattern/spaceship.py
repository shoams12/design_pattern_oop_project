class Spaceship:
    MAX_HIT_POINTS = 50


    def __init__(self, name):
        self._name = name
        self._points = Spaceship.MAX_HIT_POINTS


    @property
    def name(self):
        return self._name


    @property
    def points(self):
        return self._points


# Damage to the spaceship
    def take_damage(self, damage):
        self._points = max(0, self._points - damage)


# repairs the spaceship points
    def repair(self, points):
        self._points = min(Spaceship.MAX_HIT_POINTS, self._points + points)


# Takes points back to 50
    def reset(self):
        self._points = Spaceship.MAX_HIT_POINTS


# Checks if spaceship is destroyed
    def is_destroyed(self):
        return self._points <= 0
