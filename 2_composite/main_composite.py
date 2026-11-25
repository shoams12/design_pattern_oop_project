
from composite import Composite
from leaf import Leaf


if __name__ == '__main__':
    # Create a tree structure
    root = Composite("root", 1)
    root.add(Leaf("Leaf A", 2))
    root.add(Leaf("Leaf B", 4))

    comp = Composite("Composite X", 10)
    comp.add(Leaf("Leaf XA", 6))
    comp.add(Leaf("Leaf XB", 8))

    root.add(comp)
    root.add(Leaf("Leaf C", 12))

    # Add and remove a leaf
    leaf = Leaf("Leaf D", 7)
    root.add(leaf)
    root.remove(leaf)

    # Recursively display tree
    root.display(1)
    print()

    # Sum - not recursive
    print(f"Sum from root        = {root.sum()}")
    print(f"Sum from Composite X = {comp.sum()}")
    print(f"Sum from Leaf A      = {Leaf('Leaf A', 2).sum()}")
    print()

    # Check if all leaves are even - recursive
    print(f"All leaves even? {root.all_leaves_even()}")

    root.add(Leaf("Leaf E", 5))
    print("After adding Leaf E (5):")
    print(f"All leaves even? {root.all_leaves_even()}")

    # Wait for user
    input("Press Enter to exit...")