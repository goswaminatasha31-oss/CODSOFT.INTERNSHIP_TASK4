
import tkinter as tk

from game_logic import computer_choice, check_winner
from ui import GameUI


# Game scores
user_score = 0
computer_score = 0
draw_score = 0


# Start a new round
def play_game(user):

    global user_score, computer_score, draw_score

    computer = computer_choice()
    result = check_winner(user, computer)

    if result == "Win":
        user_score += 1

    elif result == "Lose":
        computer_score += 1

    else:
        draw_score += 1

    game.show_result(user, computer, result)

    game.update_score(
        user_score,
        draw_score,
        computer_score
    )


# Reset all scores
def reset_game():

    global user_score, computer_score, draw_score

    user_score = 0
    computer_score = 0
    draw_score = 0

    game.update_score(0, 0, 0)
    game.reset_display()


# Create application
root = tk.Tk()

game = GameUI(root, play_game, reset_game)

# Run the application
root.mainloop()
