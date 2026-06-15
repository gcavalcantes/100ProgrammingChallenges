""" Hangman Game by Gabriel Cavalcante"""
import random

def select_word():
    """Select a random word from the list of words."""
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(words)