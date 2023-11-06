from AnimalLover.Animal import AnimalLover

def test_AnimalLover_is_abstract():
    try:
        AnimalLover("micky", "cat")
    except TypeError as e:
        assert "Can't instantiate abstract class AnimalLover" in str(e)
