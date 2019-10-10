import random
import sys

def roll():
	#Rolls dice and requests user to go again.
	answer = input("Would you like to roll the dice? (yes or no): ").lower()
	
	while answer != "yes" or answer != "no":
		print("Invalid input")
		answer = input("Would you like to roll the dice again? (yes or no): ").lower()
		
		while answer == "yes":
			roll_result = random.randint(1, 6)
			print("Dice Roll: " + str(roll_result))
			answer = input("Would you like to roll the dice again? (yes or no): ").lower()
				
		if answer == "no":
			print("You have chosen not to roll the dice again. The End!")
			sys.exit()	
	
#Function Invoking
roll()

