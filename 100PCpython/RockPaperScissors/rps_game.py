"""Rock Paper Scissors Game by Gabriel Cavalcante"""

import random

def get_user_choice():
    """Get the user's choice of rock, paper, or scissors."""
    player_choice: str = ""
    while player_choice not in ["r", "p", "s", "rock", "paper", "scissors"]:
        player_choice = str(input("Enter your choice (rock, paper, scissors): ")).lower()
    return player_choice

def get_computer_choice():
    """Randomly generate the computer's choice of rock, paper, or scissors."""
    computer_choice: str = random.choice(["rock", "paper", "scissors"])
    return computer_choice
