from collections import Counter
import os
import random


def word_list_handler(filename='10000-words.txt'):
	word_lst = []

	with open(filename, 'r') as words:
		for word in words:
			if len(word.strip()) == 5 and not word[0].isupper():
				word_lst.append(word.strip())
	
	return word_lst

def word_picker(lst):
	word = random.choice(lst).lower()
	return word

def game(word):
	game_display()

	guess_count = 0
	score = 0

	while True:
		guess = ask_for_word()

		length = len(guess)
		if length == 5:
			guess_count += 1
		if guess == word:
			break
		score = checker(guess, word)

		if guess == 'cheater':
			print('The word is ' + word + '. Press any key to continue...')
			input()

		game_display()
		display_status(guess_count, score, guess, length)
		
	print(f'\nYou won! The word was {word}.\n')

def game_display():
	os.system('clear')
	print('The computer has chosen a 5 letter word. Can you guess what it is?\n')

def ask_for_word():
	word = input("What is your guess? ").lower()
	return word

def checker(word1, word2):
	word1_cnt = Counter(word1)
	word2_cnt = Counter(word2)
	intersect = word1_cnt & word2_cnt

	result = sum(intersect.values())

	return result

def display_status(guess_count, common_letters, guessed_word='', length=5):
	print(f'You have made {guess_count} guesses so far.')
	if length != 5:
		print('Make sure your guess is 5 characters long.')
		pass
	else:
		print(f'There were {common_letters} common letters between your guess ' +
		'and your target.')


if __name__ == '__main__':
	word_lst = word_list_handler()
	word_to_guess = word_picker(word_lst)

	game(word_to_guess)