'''
Program to calculate a person's age
by Gabriel Cavalcante
'''
from datetime import datetime


class Calc_age:
    def calc_age():
        print("===================================================")
        print("Program to calculate a person's age or the year they were born.")

        exit = False
        while not exit:

            # Offers the options finding out a person's age or the year they were born.
            # Makes sure that the option is not in capital letters
            opt: str = input(
                "Would you like to find out a person's age (a) or the year they were born (b) ?\n").lower()
            # If option 'a' is chosen
            if opt == "a":
                person_age = age()
                print(
                    "This person is between {} and {} years of age.".format(person_age-1, person_age))
            # If option 'b' is chosen
            elif opt == "b":
                born_year = year()
                print("This person was born in {}n".format(born_year))
            # If the input is incorrect
            else:
                print("Option unavailable.")

            question: str = input(
                "Would you like to continue to calculate someone's age? (y/n) \n").lower()

            if question == "n" or question == "no":
                exit = True
        print("End of the program...\n===================================================")

    # Function to calculate a person's age.
    def age():
        year_born: int = int(
            input("What year was this person born in? \n"))
        full_date = datetime.now()
        year = int(full_date[0])
        years_old = int(year - year_born)
        return years_old

    # Function to calculate the year of birth.
    def year():
        age = input(input("Whats the person's age? \n"))
        full_date = datetime.now()
        year = int(full_date[0])
        born_in = int(year - int(age))
        return born_in

    # Calls the main function
    calc_age()


# New instance of the Calc_age class
calculate_age = Calc_age()
calculate_age()
