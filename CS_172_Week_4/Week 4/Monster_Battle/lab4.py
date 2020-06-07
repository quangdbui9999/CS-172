#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from monster import *
from Tom import Monster1
from Jerry import Monster2
from Periwinkle import Monster3
from Cilantro import Monster4
import random

class Tournament:
	def __init__(self, m1 = Monster1(), m2 = Monster2):
		self.__m1 = m1
		self.__m2 = m2

	#This function has two monsters fight and returns the winner
	def monster_battle(self,):

		#first reset everyone's health!
		self.__m1.resetHealth()
		self.__m2.resetHealth()

		#next print out who is battling
		print("Starting Battle Between")
		print(self.__m1.getName()+": "+ self.__m1.getDescription())
		print(self.__m2.getName()+": "+ self.__m2.getDescription())


		#Whose turn is it?
		attacker = None
		defender = None

		#Select Randomly whether m1 or m2 is the initial attacker
		#to other is the initial definder
		initial_attacker = random.randrange(1, 3)
		if initial_attacker == 1:
			attacker = self.__m1
			defender = self.__m2
		elif initial_attacker == 2:
			attacker = self.__m2
			defender = self.__m1


		print(attacker.getName()+" goes first.\n")
		#Loop until either 1 is unconscious or timeout
		while( self.__m1.getHealth() > 0 and self.__m2.getHealth() > 0):
			#Determine what move the monster makes
			#Probabilities:
			#	60% chance of standard attack
			#	20% chance of defense move
			#	20% chance of special attack move

			#Pick a number between 1 and 100
			move = random.randint(1,100)
			#It will be nice for output to record the damage done
			before_health = defender.getHealth()

			#for each of these options, apply the appropriate attack and
			#print out who did what attack on whom
			if(move >=1 and move <= 60):
				# Attacker uses basic attack on defender
				attacker.basicAttack(defender)
				print(f"{attacker.getName()} used {attacker.basicName()} on {defender.getName()}")
			elif (move>=61 and move <= 80):
				# Defend!
				attacker.defenseAttack(defender)
				print(f"{attacker.getName()} used {attacker.defenseName()} on {defender.getName()}")
			else:
				# Special Attack!
				attacker.specialAttack(defender)
				print(f"{attacker.getName()} used {attacker.specialName()} on {defender.getName()}")
			#Swap attacker and defender
			temp = attacker
			attacker = defender
			defender = temp

			#Print the names and healths after this round
			print(f"{self.__m1.getName()} at {self.__m1.getHealth()}")
			print(f"{self.__m2.getName()} at {self.__m2.getHealth()}\n")


		#Return who won
		if(self.__m1.getHealth() <= 0):
			print(f"{self.__m2.getName()} is victorious!")
			return self.__m2
		elif(self.__m2.getHealth() <= 0):
			print(f"{self.__m1.getName()} is victorious!")
			return self.__m1

#----------------------------------------------------
if __name__=="__main__":
	first = Monster1("Tom")
	second = Monster2("Jerry")
	third = Monster3("Periwinkle")
	fourth = Monster4("Cilantro")

	battle1 = Tournament(first, second)
	battle2 = Tournament(third, fourth)

	print("Round 1\n")
	winner1 = battle1.monster_battle()
	print("\n\nRound 2\n")
	winner2 = battle2.monster_battle()
	print("\n\nRound 3\n")
	finalBattle = Tournament(winner1, winner2)
	winner = finalBattle.monster_battle()
	#Print out who won
	####TODO####
	