from my_set import MySet

set_of_structures = MySet()

set_of_structures.add((1, 2))
set_of_structures.add((1, 2))
set_of_structures.add((2, 1))

for element in set_of_structures:
    print(element)

# set_of_structures.add([1, 2]) unhashable type: 'list'