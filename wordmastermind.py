from collections import Counter
import os
import random
import string

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
	intro_display()

	guess_count = 0
	score = 0

	guesses_list = []
	alphabet = string.ascii_uppercase

	while True:
		guess = ask_for_word()
		length = len(guess)

		if guess == 'cheater':
			print('The word is ' + word + '. Press any key to continue...')
			input()
			continue

		if length == 5:
			guess_count += 1
		else:
			print('Make sure your guess is 5 characters long.\n')
			continue
		
		if guess == word:
			break
		
		alphabet = alph_compare(guess, alphabet)

		score = checker(guess, word)
		guesses_list.append((guess, score))

		intro_display()
		display_status(guess_count, score, guesses_list, 
			alphabet, guess, length)
		
	print(f'\nYou won! The word was {word}.\n')

def intro_display():
	os.system('clear')
	print('The computer has chosen a 5 letter word. Can you guess what it is?\n')

def ask_for_word():
	word = input("What is your guess? ").lower()
	return word

def alph_compare(guess, alph):
	for char in guess.upper():
		if char in alph:
			alph = alph.replace(char, '')

	return alph

def checker(word1, word2):
	word1_cnt = Counter(word1)
	word2_cnt = Counter(word2)
	intersect = word1_cnt & word2_cnt

	result = sum(intersect.values())

	return result

def display_status(guess_count, common_letters, guesses_list, alphabet_used, guessed_word='', length=5):
	print(f'You have made {guess_count} guesses so far.')
	print(f'There were {common_letters} common letters between the word ' +
		f'\'{guessed_word}\' and your target.')
	print(f'Letters guessed: {alphabet_used}\n')
	for word, score in guesses_list[-10:]:
		print(word + ':' + str(score))
	print()

if __name__ == '__main__':
	word_lst = word_list_handler()
	word_to_guess = word_picker(word_lst)

	game(word_to_guess)