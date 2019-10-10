#HangmanV1 Created by YesIamPro
import random

def main():
	print('--------------------------------------------------------------------------------')
	print('																					')
	print('																					')
	print('			Welcome to Hangman V1													')
	print('				Created by YesIamPro												')
	print('																					')
	print('--------------------------------------------------------------------------------')
	
	while True:
		print('Would you like to start game? (yes or no)')
		answer = input('Answer: ').lower()
				
		if answer == 'yes':
			play()
		elif answer == 'no':
			print('Game Ended')
			return
		else:
			print('Invalid Input')
	
def play():
	#List of available words used for play.
	word_list = ['hangman']
	#Random word selection.
	word = random.choice(word_list)

	#Splits word into list format.
	word_list = list(word)
	#Retrieves amount of characters in word
	word_characters = len(word)
	#Creates list which stores correct user input. To be compared with word_list
	user_guessed_word_list = []
	#List is converted and stored in string. To be compraed with word variable.
	user_guessed_word = ''
	
	#Creates appropriate sized list to store the users correct guesses. 
	for x in range (0,word_characters): 
		user_guessed_word_list.append(' ')
	
	print('\nHow many lives would you like? (Recomended 6 minimum)')
	life = int(input('Answer: '))
	
	print(f'\nThe word has {word_characters} characters')
	
	while user_guessed_word != word or life != 0:
		print(f'Word Discoverd: {user_guessed_word}')
		guessed_letter = input('Please enter a letter you would like to guess: ').lower()
		if guessed_letter in word_list:
			letter_count = word_list.count(guessed_letter)
			if letter_count == 1:
				letter_index = word_list.index(guessed_letter)
				user_guessed_word_list[letter_index] = guessed_letter
				word_list[letter_index] = ''
				user_guessed_word = "".join(user_guessed_word_list)
				print('\nWell Done. You guessed correctly!\n')
			elif letter_count > 1:
				for x in range(0, letter_count):
					letter_index = word_list.index(guessed_letter)
					user_guessed_word_list[letter_index] = guessed_letter
					word_list[letter_index] = ''
					user_guessed_word = "".join(user_guessed_word_list)
				print('\nWell Done. You guessed correctly!\n')
		#If letter is not in selected word it deducts a life.
		elif guessed_letter not in word_list:
			life = life - 1
			print(f'You have lost a life. You have {life} lives remaining!')   
		#If letter is in selected word, it adds that letter to the users guessed word.
				
		#End game if user life reaches 0.
		if life == 0:
			print('You have ran out of lives')
			return
			
		#End game if user correctly guesses the word.
		if user_guessed_word == word:
			print('*' * 75)
			print(f'\nYou have guessed the word correctly. The word is {word}.\n')	
			print('*' * 75)
			return	

#Invoke Functions
main()





