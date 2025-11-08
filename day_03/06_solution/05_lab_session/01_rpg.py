import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, health=10, defense=10):
        self._health = health
        self._defense = defense
        self._skill_used = False

    @property
    def is_alive(self):
        return self._health > 0

    @property
    def health(self):
        return self._health

    @abstractmethod
    def attack(self, other):
        raise NotImplementedError()

    @abstractmethod
    def use_skill(self, other):
        raise NotImplementedError()

    @abstractmethod
    def __str__(self):
        raise NotImplementedError()


class Knight(Character):
    def __init__(self, health, defense):
        super().__init__(health, defense)

    def attack(self, other: Character):
        damage = max(1, self._defense - other._defense)
        other._health -= damage
        print(f"Knight attacks! Deals {damage} damage.")

    def use_skill(self, other):
        if self._skill_used:
            print("Fortify already used!")
            return
        self._defense += 5
        self._skill_used = True
        print("Knight uses Fortify! Defense increases by 5 permanently.")

    def __str__(self):
        return f"Knight(HP: {self._health}, DEF: {self._defense})"


class Mage(Character):
    def __init__(self, health, defense, magic):
        super().__init__(health, defense)
        self._magic = magic

    def attack(self, other: Character):
        damage = max(1, self._magic - other._defense)
        other._health -= damage
        print(f"Mage casts spell! Deals {damage} damage.")

    def use_skill(self, other):
        if self._skill_used:
            print("Fireball already used!")
            return
        damage = self._magic + 15
        other._health -= damage
        self._skill_used = True
        print(f"Mage casts Fireball! Massive explosion! Deals {damage} damage.")

    def __str__(self):
        return f"Mage(HP: {self._health}, DEF: {self._defense}, MAG: {self._magic})"


class Warrior(Character):
    def __init__(self, health, defense, strength):
        super().__init__(health, defense)
        self._strength = strength

    def attack(self, other: Character):
        damage = max(1, self._strength - other._defense)
        other._health -= damage
        print(f"Warrior strikes! Deals {damage} damage.")

    def use_skill(self, other):
        if self._skill_used:
            print("Rage already used!")
            return
        self._strength += 5
        self._skill_used = True
        print("Warrior uses Rage! Strength increases by 5 permanently.")

    def __str__(self):
        return f"Warrior(HP: {self._health}, DEF: {self._defense}, STR: {self._strength})"


class Game:
    def __init__(self):
        self.player = None
        self.enemy = None

    def generate_character(self, char_class):
        hp = random.randint(20, 30)
        defense = random.randint(5, 15)

        if char_class == Knight:
            return Knight(hp, defense)
        elif char_class == Mage:
            magic = random.randint(15, 25)
            return Mage(hp, defense, magic)
        elif char_class == Warrior:
            strength = random.randint(15, 25)
            return Warrior(hp, defense, strength)

    def select_player(self):
        print("Choose your character:")
        options = [Knight, Mage, Warrior]
        generated = [self.generate_character(cls) for cls in options]
        for idx, char in enumerate(generated):
            print(f"{idx + 1}. {char}")
        while True:
            try:
                choice = int(input("Enter number: ")) - 1
                if 0 <= choice < len(generated):
                    self.player = generated[choice]
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Not a number.")

    def generate_enemy(self):
        enemy_cls = random.choice([Knight, Mage, Warrior])
        self.enemy = self.generate_character(enemy_cls)
        print(f"\nA wild enemy appears!\nEnemy: {self.enemy}")

    def player_turn(self):
        print("\n--- Your Turn ---")
        print(f"Your HP: {self.player.health} | Enemy HP: {self.enemy.health}")
        print("1. Attack")
        print("2. Use Skill")
        action = input("Choose action: ")

        if action == "1":
            self.player.attack(self.enemy)
        elif action == "2":
            self.player.use_skill(self.enemy)
        else:
            print("You trip and miss your turn.")

    def enemy_turn(self):
        print("\n--- Enemy Turn ---")
        self.enemy.attack(self.player)

    def battle_loop(self):
        while self.player.is_alive:
            self.generate_enemy()

            while self.player.is_alive and self.enemy.is_alive:
                self.player_turn()
                if self.enemy.is_alive:
                    self.enemy_turn()

            if self.player.is_alive:
                print("\nYou defeated the enemy! (=3=)")
                # Optional healing
                heal = min(10, 30 - self.player.health)
                self.player._health += heal
                print(f"You rest and recover {heal} HP.\n")
                input("Press Enter... Another challenger approaches!")
            else:
                print("\n=== Game Over ===")
                print("You died. (x_x)")

    def start(self):
        print("=== Welcome to RPG Lite ===")
        self.select_player()
        self.battle_loop()


if __name__ == "__main__":
    game = Game()
    game.start()
