import random

print("We are going to play between a range from 1 to 25. Choose your secret number!")

ready = "no"

while ready == "no":
    ready = input("Are you ready?\nPlease type 'yes' or 'no'")

if ready != "yes":
    print("Dummy, you made a typo!")
    ready = "no"

guess = "no"

while guess == "no":
    guessed_number = random.randint(1,25)
    #How can I make the computer choose unique random numbers?

    guess = input(f"My guess is {guessed_number}. Is it correct?\nPlease type 'yes' or 'no'")

if guess != "yes":
    print("Dummy, you made a typo!")
    guess = "no"

if guess == "yes":
    print("Congrats to me! I have guessed the number correctly!")