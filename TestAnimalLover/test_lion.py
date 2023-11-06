from AnimalLover.lion import lion

Lion = lion("Don", "Lion", "Golden","100")

def test_lion_make_sound():
    assert Lion.make_sound() == "It roars"

def test_lion_move():
    assert Lion.move() == "It moves very very fast"
