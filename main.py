from AnimalLover.dog import dog
from AnimalLover.lion import lion
from AnimalLover.parrot import parrot

Dog = dog("scupy", "Dog", "white")
Lion = lion("Don", "Lion", "100")
Parrot = parrot("cutie", "Parrot", "6")


print(Dog.make_sound())
print(Dog.move())
print(Lion.make_sound())
print(Lion.move())
print(Parrot.make_sound())
print(Parrot.move())
