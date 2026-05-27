'''
Program to calculate a person's age in senconds
by Gabriel Cavalcante
'''
from datetime import datetime


class Calc_age:
    def calc_age(self):
        print("===================================================")
        print("Program to calculate a person's age in seconds.")

        exit = False
        while not exit:

            # Offers the options finding out a person's age or the year they were born.
            # Makes sure that the option is not in capital letters
            person_age = self.age()
            print(
                    "This person is {} seconds old.".format(person_age))
            # If option 'b' is chosen
            
            question: str = input(
                "Would you like to continue to calculate someone's age? (y/n) \n").lower()

            if question == "n" or question == "no":
                exit = True
        print("End of the program...\n===================================================")

    # Function to calculate a person's age.
    def age(self):
        year_born: int = int(
            input("What year was this person born in? \n"))
        full_date = datetime.now()
        year = int(full_date.year)
        years_old = int(year - year_born)
        # Calculate age in seconds
        age_in_seconds = years_old * 365 * 24 * 60 * 60
        return age_in_seconds

    # Calls the main function
    def __init__(self):
        self.calc_age()


# New instance of the Calc_age class
calculate_age = Calc_age()

# End of the program