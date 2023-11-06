from AnimalLover.Animal import AnimalLover

class dog(AnimalLover):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def make_sound(self):
        return f"It barks"
      
    def move(self):
        return f"It moves very fast"