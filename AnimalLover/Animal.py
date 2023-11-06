from abc import ABC, abstractmethod

# Define the abstract parent class 'AnimalLover'
class AnimalLover(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species
       
        
    @property
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass

