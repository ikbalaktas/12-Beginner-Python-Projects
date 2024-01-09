import random

def rps_game():

    user = input("Type 'r' for rock, 'p' for paper, 's' for scissors.")
    computer = random.choice(["r", "p", "s"])
        
    if user == computer:
        return "It's a tie!"

    if winner(user, computer):
        return "You won!"

    return "Computer won!"

def winner(player, opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s"  and opponent == "p"):
        return True
    
print(rps_game())