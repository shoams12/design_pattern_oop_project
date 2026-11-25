from component import Component


class Leaf(Component):

    def add(self, component):
        print("Cannot add to a leaf")

    def remove(self, component):
        print("Cannot remove from a leaf")

    def get_children(self):
        return []

    def display(self, depth):
        print("-" * depth + f"{self._name} ({self._number})")

    def all_leaves_even(self):
        # תנאי העצירה של הרקורסיה
        return self._number % 2 == 0