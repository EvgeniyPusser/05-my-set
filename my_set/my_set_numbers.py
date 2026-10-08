from my_set import MySet

set_of_numbers = MySet(capacity=30)

print(set_of_numbers.add(10))
print(set_of_numbers.add(20))
print(set_of_numbers.add(10))

print(10 in set_of_numbers)
print(30 in set_of_numbers)

print(len(set_of_numbers))

for element in set_of_numbers:
    print(element)