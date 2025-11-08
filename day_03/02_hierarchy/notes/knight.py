class Character:
	def __init__(self, health=100, defense=10):
		self.health = health
		self.defense = defense

	def attack(self, other):
		damage = 20 - other.defense
		other.health -= damage

class Knight:
	def __init__(self, health=10, defense=10):
		self.health = health
		self.defense = defense

	def attack(self, other):
		damage = self.defense - other.defense
		other.health -= damage

player = Knight(defense=30)
enemy = Character()

player.attack(enemy)
print(enemy.health)