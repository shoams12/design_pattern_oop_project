from abc import ABC, abstractmethod


class Component(ABC):

    def __init__(self, name, number):
        self._name = name
        self._number = number

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number

    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def get_children(self):
        pass

    @abstractmethod
    def display(self, depth):
        pass

    @abstractmethod
    def all_leaves_even(self):
        pass

    def sum(self):
        total = 0
        stack = [self]

        while stack:
            current = stack.pop()
            total += current.number
            stack.extend(current.get_children())

        return total