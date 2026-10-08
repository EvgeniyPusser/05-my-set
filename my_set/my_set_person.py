from my_set import MySet
from dataclasses import dataclass, field

@dataclass(unsafe_hash=True, frozen=True)
class Person:
    id: int
    name: str = field(compare=False)

    # def __init__(self, id, name):
    #     self.id = id
    #     self.name = name

    def __str__(self):
        return f'Person(id={self.id}, name={self.name})'

    # def __hash__(self):
    #     return hash(self.id)
    #
    # def __eq__(self, other):
    #     if not isinstance(other, Person):
    #         return False
    #     return self.id == other.id


p1 = Person(1, 'John')
p2 = Person(2, 'Jane')
p3 = Person(1, 'John')

my_set_of_person = MySet()

my_set_of_person.add(p1)
my_set_of_person.add(p2)
my_set_of_person.add(p3)

for item in my_set_of_person:
    print(item, hash(item))

# Problem: p1.id is changed after adding it to the set, so the hash value changes and the set no longer contains p1
# p1.id = 2
#
# for item in my_set_of_person:
#     print(item, hash(item))