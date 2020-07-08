# wordmastermind Overview - letters guessed feature
---

**Describe what your feature will do in abstract terms, as if it was a person doing it, not a computer.**

Program will display a list that shows which letters have not been guessed yet. As the user guesses a word, Program will go to his alphabet list and remove any of the guessed letters.

**From there, now describe how your feature will handle data. Start BIG as possible.**

The feature will take in each guess and remove any letters guessed that are still present in the list. IN: string, guess; OUT: none (edited list)

**Break down the process further in abstract terms. What are the distinct actions it will need to take? What would a random stupid guy need if you wanted him to do it?**

- Program will get user guess and alphabet list
- Program will compare letters in user guess to alphabet list
- Any letters that are present in both will be removed from the alphabet list