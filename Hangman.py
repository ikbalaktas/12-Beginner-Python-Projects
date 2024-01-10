from words import words
import random
import string

def choose_valid_word(words):

    word = random.choice(words)
    while " " or "-" in word:
        word = random.choice(words)
        return word.upper()
    
def hangman():
    
    lives = 6
    word = choose_valid_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word)
    used_letters = set()

    while lives > 0 and len(word_letters) > 0:

        print("You have", lives, "lives left and you have used these letters:", " ".join(used_letters))

        current_word = [letter if letter in used_letters else "-" for letter in word]
        print("Current word is", current_word)

        guess = input("Guess a letter:").upper()

        if guess in alphabet - used_letters:
            used_letters.add(guess)

            if guess in word_letters:
                word_letters.remove(guess)

                if  len(word_letters) == 0:
                    print("Congrats! You have guessed the word", word, "correctly!")
                else:
                    print("Your guess is correct!")

            else:
                lives = lives - 1

                if lives == 0:
                    print("Sorry, you have lost the game!\nThe word was:", word)
                "You have guessed the letter wrong! Please try again."

        elif guess in used_letters:
            print("You have already guessed that letter")

        else:
            print("You have guessed an invalid character.")

hangman()