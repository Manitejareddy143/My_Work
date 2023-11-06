from AnimalLover.parrot import parrot

Parrot = parrot("cutie", "Parrot", "6")

def test_parrot_make_sound():
    assert Parrot.make_sound() == "It gurgles and trills"

def test_parrot_move():
    assert Parrot.move() == "It moves very fast in air"
