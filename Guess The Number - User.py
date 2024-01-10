import random

x = int(input("Select the range you want to play in between: \nFrom: "))

while x <= 0:
    print("Error! Values need to be positive.")
    x = int(input("Please select starting point again: "))

y = int(input("To: "))

while y <= x:
    print("Error! Endpoint must be greater than starting point.")
    y = int(input("Please select end point again: "))

while y == x+1:
    print("Error! There are no integers between given values.")
    y = int(input("Please select end point again: "))


random_number = random.randint(x,y)
guess = 0

while guess != random_number:
    guess = int(input("Let us hear your guess!"))

    if guess < x:
        print(f"Dummy, you forgot the starting point {x}.")

    elif guess > y:
        print(f"Dummy, you forgot the end point {y}.")
    
    elif guess < random_number:
        print("Sorry, your guess is too low.")

    elif guess > random_number:
        print("Sorry, your guess is too high.")

print(f"Congrats! You've guessed the number {random_number} correctly.")