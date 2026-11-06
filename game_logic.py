import random
choices = ["Rock", "Paper", "Scissors"]
def computer_choice():
    return random.choice(choices)
def check_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):
        return "Win"
    else:
        return "Lose"