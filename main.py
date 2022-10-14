import random
import string
from word import word

def get_valid_word():
    pick = random.choice(word)
    while '-' in pick or ' ' in pick:
        pick = random.choice(word)
    return pick

def hangman():
    pick = get_valid_word().upper()
    # hangman's hp
    lives = 5
    # keep the track of letters in the word
    word_letters = set(pick)
    # valid letter
    alphabet = set(string.ascii_uppercase)
    # what the user picked
    used_letters = set()
    # getting user input while the word exists
    while len(word_letters) > 0 and lives > 0:
        # show letters used
        print(f"You have {lives} lives left ")
        if len(used_letters) > 0:
            print("You have used these letters: ", " ".join(used_letters))

        # show current word
        word_list = [letter if letter in used_letters else '-' for letter in pick]
        print(f'Current word: ', " ".join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                
            else:
                lives = lives - 1
                print("Letter is not in the word")
                
        elif user_letter in used_letters:
            print(f"You have already used the letter '{user_letter}.\n")
            print(f"Please pick something else.")
            
        else:
            print(f"Invalid character, try again!")
            
    if lives == 0: 
        print("You have no more lives... Game over!")
    else:
        print("Congrats! You guess the word: ", pick)

user_input = input("Type 'start' to play hangman...\n")

if user_input == "start":
    hangman()