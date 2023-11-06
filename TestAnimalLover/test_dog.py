from AnimalLover.dog import dog

Dog = dog("scupy", "Dog", "white")

def test_dog_make_sound():
    assert Dog.make_sound() == "It barks"

def test_dog_move():
    assert Dog.move() == "It moves very fast"

