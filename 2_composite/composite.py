from component import Component


class Composite(Component):

    def __init__(self, name, number):
        super().__init__(name, number)
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def get_children(self):
        return self._children

    def display(self, depth):
        print("-" * depth + f"{self._name} ({self._number})")

        # Recursively display child nodes
        for component in self._children:
            component.display(depth + 2)

    def all_leaves_even(self):
    #Each child checks it's leafs for even numbers
        for component in self._children:
            if not component.all_leaves_even():
                return False
        return True