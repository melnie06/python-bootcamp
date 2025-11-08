from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self.health = health
        self.defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()