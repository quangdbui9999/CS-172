from monster import *

class Monster2(monster):
	def __init__(self, name = "Jerry", health = 20, description = "He is small mouse but he is very smart"):
		monster.__init__(self)
		self.__name = name
		self.__health = health
		self.__description = description

	def __str__(self):
		return "Generic Monster Class"

	def getName(self):
		return self.__name

	def getDescription(self):
		return self.__description

	def basicAttack(self, enemy):
		self.basicName()
		damage = 1
		enemy.doDamage(damage)

	def basicName(self):
		return "Bite"

	def defenseAttack(self, enemy):
		self.defenseName()
		damage = 0
		enemy.doDamage(damage)

	def defenseName(self):
		return "Hiding Tom"

	def specialAttack(self, enemy):
		self.specialName()
		damage = 3
		enemy.doDamage(damage)
		enemy.doDamage

	def specialName(self):
		return "Ghost"

	def getHealth(self):
		if (self.__health <= 0):
			return 0
		else:
			return self.__health

	def doDamage(self, damage):
		self.__health -= damage

	def resetHealth(self):
		self.__health = 20