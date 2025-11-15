class Character:
    def __init__(self, health=100, defense=10):
        self.health = health
        self.defense = defense


    def attack(self, other):
        damage = 20 - other.defense
        other.health -= damage
        
player = Character()
enemy = Character()


print("Enemy:", enemy.health)
player.attack(enemy)
print("Enemy:", enemy.health)