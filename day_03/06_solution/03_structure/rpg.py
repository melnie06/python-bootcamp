from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

class Knight(Character):
    def attack(self, other: Character):
        damage = self._defense - other._defense
        other._health -= damage

class Mage(Character):
    def __init__(self, health=10, defense=10, magic=20):
        super().__init__(health, defense)
        self._magic = magic

    def attack(self, other: Character):
        damage = self._magic - other._defense
        other._health -= damage

class Warrior(Character):
    def __init__(self, health=10, defense=10, strength=20):
        super().__init__(health, defense)
        self._strength = strength

    def attack(self, other: Character):
        damage = self._strength - other._defense
        other._health -= damage

