# Problem Set 2, hangman.py
# Name: Julen Shrestha
# Time spent: 1 hr+

import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open("words.txt", 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
  for x in secret_word:
      if x not in letters_guessed:
        return False
  return True




def get_word_progress(secret_word, letters_guessed):
  reveal_words = ["*"]* len(secret_word)
  for i in range(len(secret_word)):
    if secret_word[i] in letters_guessed:
      reveal_words[i] = secret_word[i]
  return "".join(reveal_words)  


def get_available_letters(letters_guessed):
  letters_available = []
  all_letters = string.ascii_lowercase

  for x in all_letters:
    if x not in letters_guessed:
      letters_available.append(x)
  return "".join(letters_available)


def hangman(secret_word, with_help):
  total_guesses = 10
  letters_guessed = []
  vowels = "aeiou"
  print("Welcome to Hangman!")
  print(f"I am thinking of a word that is {len(secret_word)} letter long")
  running = True
  while running:
    print("-"*20)
    print(f"you have {total_guesses} left")
    print("Available letters:", get_available_letters(letters_guessed))
    guess = input("Please guess a letter:").lower()
    if guess == "!":
      if with_help:
        if total_guesses<3:
          print("Not enough guesses left(3 needed)")
        else:
          for_help = [x for x in secret_word if x not in letters_guessed]
          hint = random.choice(for_help)
          total_guesses-=3
          print(f"Hint = {hint}")
      else:
        print("Help is disabled")

    if not guess.isalpha() or len(guess) != 1:
       print("Invalid input")
       continue

    if guess in letters_guessed:
       print("You have already guessed that letter")
       continue

    letters_guessed.append(guess)

    if guess in secret_word:
      print("Good guess")
      print(get_word_progress(secret_word,letters_guessed))
    else:
      if guess in vowels:
        total_guesses-=2
        print(f"{guess} is not the word and u lose 2 guesses")
        print(get_word_progress(secret_word,letters_guessed))
      else:
         total_guesses-=1
         print(f"{guess} is not the word and you lose 1 guess")
         print(get_word_progress(secret_word,letters_guessed))
    
    #condition check to end game
    winning_condition = has_player_won(secret_word,letters_guessed)
    if winning_condition:
        print("-"*20)
        print("Congratulations, you won!")
        running = False
    if total_guesses<=0:
      print("Sorry, you're out of guesses. The word was:", secret_word)
      break




if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    print(secret_word)
    with_help = False
    hangman(secret_word, with_help)

