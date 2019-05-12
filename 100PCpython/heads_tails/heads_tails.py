from random import *

print("========================================================\n"
      + "COIN TOSS SIMULATOR PROGRAM\nBY GABRIEL CAVALCANTE")


def coin_toss():
    #coin = {1: "Head", 2: "Tails"}
    finalize = False
    while not finalize:
        chosen_side = input("Type 'h' Heads or 't' for Tails.\n")
        result = randint(1, 2)
        if result == 1:
            if chosen_side == "h":
                print("Coin tossed...\nHEADS. You won!\n")
            else:
                print("Coin tossed...\nHEADS. You lose.\n")
        else:
            if chosen_side == "t":
                print("Coin tossed...\nTAILS. You won!\n")
            else:
                print("Coin tossed...\nTAILS. You lose.\n")

        cont = input(
            "Would you like to continue to toss coins? ('y' or 'n')\n")
        if cont == "n":
            finalize = True

        if finalize:
            print("End of the program.\n"
                  + "========================================================")


coin_toss()
