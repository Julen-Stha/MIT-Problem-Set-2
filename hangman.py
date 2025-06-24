import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    index = random.randint(0, len(wordlist) - 1)
    return wordlist[index]

def has_player_won(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

def get_word_progress(secret_word, letters_guessed):
    progress = []
    for c in secret_word:
        if c in letters_guessed:
            progress.append(c)
        else:
            progress.append("*")
    return "".join(progress)

def get_available_letters(letters_guessed):
    available_letters = []
    for c in string.ascii_lowercase:
        if c not in letters_guessed:
            available_letters.append(c)
    return "".join(available_letters)

def calculate_score(guesses_remaining, secret_word):
    unique_letters_set = set()
    for letter in secret_word:
        unique_letters_set.add(letter)
    unique_letters = len(unique_letters_set)
    word_length = len(secret_word)
    total_score = (guesses_remaining + 4 * unique_letters) + (3 * word_length)
    return total_score

def hangman(secret_word, with_help):
    total_guesses = 10
    letters_guessed = []
    vowels = "aeiou"

    print("Welcome to hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letter{'s' if len(secret_word) != 1 else ''} long.")

    while True:
        print("------")
        if total_guesses == 1:
            print(f"You have {total_guesses} guess left.")
        else:
            print(f"You have {total_guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()

        if guess == "!":
            if with_help:
                if total_guesses < 3:
                    print("Not enough guesses left (3 needed).")
                else:
                    hint_options = []
                    for c in secret_word:
                        if c not in letters_guessed:
                            if c not in hint_options:
                                hint_options.append(c)
                    if len(hint_options) > 0:
                        hint = random.choice(hint_options)
                        letters_guessed.append(hint)
                        total_guesses -= 3
                        print(f"Letter revealed: {hint}")
                        print(get_word_progress(secret_word, letters_guessed))
                        if has_player_won(secret_word, letters_guessed):
                            print("------")
                            score = calculate_score(total_guesses, secret_word)
                            print("Congratulations, you won!")
                            print(f"Your total score for this game is: {score}")
                            break
                    else:
                        print("No more letters to reveal.")
            else:
                print("Help is disabled.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single alphabet letter.")
            continue

        if guess in letters_guessed:
            print("You have already guessed that letter.")
            continue

        letters_guessed.append(guess)

        if guess in secret_word:
            print("Good guess:", get_word_progress(secret_word, letters_guessed))
        else:
            if guess in vowels:
                total_guesses -= 2
            else:
                total_guesses -= 1
            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")

        if has_player_won(secret_word, letters_guessed):
            print("------")
            score = calculate_score(total_guesses, secret_word)
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {score}")
            break

        if total_guesses <= 0:
            print("-------")
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            break

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist)
    # print(secret_word)
    with_help = True
    hangman(secret_word, with_help)
