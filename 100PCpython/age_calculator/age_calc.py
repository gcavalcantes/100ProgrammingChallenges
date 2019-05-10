'''
Program to calculate a person's age
by Gabriel Cavalcante
'''
from datetime import datetime


class Calc_age:
    def calc_age(self):
        print("===================================================")
        print("Program to calculate a person's age or the year they were born.")

        ex = False
        while not ex:

            # Offers the options finding out a person's age or the year they were born.
            # Makes sure that the option is not in capital letters
            opt: str = input(
                "Would you like to find out a person's age (a) or the year they were born (b) ?\n").lower()
            # If option 'a' is chosen
            if opt == "a":
                year_born: int = int(input("What year was this person born in? \n"))
                full_date = datetime.now()
                year = int(full_date[0])
                age = year - year_born
                print("This person has between {} and {} years of age.".format(age-1, age))
            # If option 'b' is chosen
            elif opt == "b":
                age = input("Whats the person's age? \n")
                full_date = datetime.now()
                year = int(full_date[0])
                print("This person was born in {}n".format(year - int(age)))
            # If the input is incorrect
            else:
                print("Option unavailable.")

            question: str = input(
                "Would you like to continue to calculate a person's age? (y/n) \n").lower()

            if question == "n" or question == "no":
                ex = True
        print("End of the program...\n===================================================")
