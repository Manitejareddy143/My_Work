from AnimalLover.Animal import AnimalLover

class parrot(AnimalLover):
    def __init__(self, name, species, age):
        super().__init__(name, species)
        self.age = age

    def make_sound(self):
        return f"It gurgles and trills"
      
    def move(self):
        return f"It moves very fast in air"
