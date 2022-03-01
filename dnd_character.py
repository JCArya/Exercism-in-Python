from random import randint
def modifier(n):
	return (n - 10) // 2
class Character:
	def __init__(self):
		self.strength = self.ability()
		self.dexterity = self.ability()
		self.constitution = self.ability()
		self.intelligence = self.ability()
		self.wisdom = self.ability()
		self.charisma = self.ability()
		self.hitpoints = modifier(self.constitution) + 10
	
	def ability(self):
		return sum(sorted(randint(1, 6) for _ in range(4))[1:])
