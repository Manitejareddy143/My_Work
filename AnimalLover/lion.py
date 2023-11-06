from AnimalLover.Animal import AnimalLover

class lion(AnimalLover):
    def __init__(self, name, species, weight):
        super().__init__(name, species)
        self.weight = weight

    def make_sound(self):
        return f"It roars"
      
    def move(self):
        return f"It moves very very fast"
