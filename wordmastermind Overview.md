#Wordsmash Explosion
---

**Describe what your program will do in abstract terms, as if it was a person doing it, not a computer.**

Program will pick a random 5 letter word that the user will try to guess. The user will guess a 5 letter word and Program will return how many of the letters from user's word exist in Program's word. This process will repeat until the user guesses the word correctly.

**From there, now describe how your program will handle data. Start BIG as possible.**

IN: built in word list
OUT: n/a

**Break down the process further in abstract terms. What are the distinct actions it will need to take? What would a random stupid guy need if you wanted him to do it?**

- Program opens built-in word list and makes a list of all the 5-letter words.
- Program chooses a random word from this list as their chosen word.
- Program asks user for guess of the word.
- Program tests the letters of user's word against Program's word and returns how many letters there are in common (unordered).
- This repeats until user guesses the correct word, in which it quits.

**Determine the biggest distinct functions you can perceive in the description you just created.**

Random Word Picker - Picks random word from word list
Asker - Asks user for their guess
Checker - Checks user word against Program's word
Display - Shows on screen the chosen word and how many similar letters there are

**What data types would be best to transfer in between these functions?**

Random Word Picker
	* IN: words file
	* OUT: string of program's chosen word

Asker:
	* IN: None
	* OUT: string of user's chosen word

Checker:
	* IN: strings (2) of user's and program's chosen words
	* OUT: int of common letters between the words

Display:
	* IN: string of user's chosen word, and int of common letters
	* OUT: None

