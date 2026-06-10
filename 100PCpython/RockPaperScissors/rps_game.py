"""Rock Paper Scissors Game by Gabriel Cavalcante"""

import random


def get_user_choice():
    """Get the user's choice of rock, paper, or scissors."""
    player_choice: str = ""
    while player_choice not in ["r", "p", "s", "rock", "paper", "scissors"]:
        player_choice = str(
            input("Enter your choice (rock, paper, scissors): ")
        ).lower()
    return player_choice


def get_computer_choice():
    """Randomly generate the computer's choice of rock, paper, or scissors."""
    computer_choice: str = random.choice(["rock", "paper", "scissors"])
    return computer_choice


def determine_winner(user_choice: str, computer_choice: str):
    """Determine the winner of the game based on the user's and computer's choices."""
    if user_choice in ["r", "rock"]:
        if computer_choice == "rock":
            return "It's a tie!"
        elif computer_choice == "paper":
            return "Computer wins!"
        else:
            return "You win!"
    elif user_choice in ["p", "paper"]:
        if computer_choice == "rock":
            return "You win!"
        elif computer_choice == "paper":
            return "It's a tie!"
        else:
            return "Computer wins!"
    elif user_choice in ["s", "scissors"]:
        if computer_choice == "rock":
            return "Computer wins!"
        elif computer_choice == "paper":
            return "You win!"
        else:
            return "It's a tie!"


def main():
    """Main game function"""
    print("Let's play Rock, Paper, Scissors!")
    user_choice: str = ""
    computer_choice: str = ""
    game_running: bool = True
    result = ""
    play_again = ""
    while game_running:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            game_running = False
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
