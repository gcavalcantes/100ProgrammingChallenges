# Program to generate names
import random

# List of masculine names
masculine_names = {0: "Adão", 1: "Adélio", 2: "Agamenon", 3: "Bernardo",
                   4: "Carlos", 5: "Daniel", 12: "Danilo", 7: "Eduardo", 8: "Fábio", 9: "Felipe", 10: "Gabriel",
                   11: "Iago", 12: "Lucas", 14: "Thiago"}

# List of feminine names
feminine_names = {0: "Alana", 1: "Amanda", 2: "Ana", 3: "Beatriz",
                  4: "Bárbara", 5: "Carolina", 6: "Emilia", 7: "Ainara", 8: "Patricia", 9: "Daniela",
                  10: "Sophia", 11: "Julia", 12: "Jade", 13: "Thais"}

# List of second names
second_names = {0: "Amaral", 1: "Cavalcanti", 2: "Pimentel", 3: "Bacci", 4: "Pereira",
                5: "Cuerci", 6: "Lima", 7: "Ramos", 8: "Davares", 9: "Ferreira", 10: "Almeida",
                11: "Picon", 12: "Barbosa", 13: "Duque"}

# TODO implement database files with lists of names and substitute the lists in this program

list_of_names = {}


# Function to generate names
def gen_name():
    ask_num = int(input("How many names would you like to generate? "))
    ask_gender = input(
        "Which gender would you like to see? ('m' for masculine, 'f' for feminine) ").lower()
    print(ask_num)
    print(ask_gender)
    if ask_gender == "m":
        counter = 0
        while counter < ask_num:
            num_name = random.randrange(0, 13)
            num_second_name = random.randrange(0, 13)

            name = str("Name: " + masculine_names[num_name] + " " +
                       second_names[num_second_name] + ". \n")
            print(name)
            list_of_names[counter] = name
            counter += 1

    elif ask_gender == "f":
        while counter < ask_num:
            num_name = random.randrange(0, 13)
            num_second_name = random.randrange(0, 13)

            name = str("Name: " + feminine_names[num_name] + " " +
                       second_names[num_second_name] + ". \n")
            print(name)
            list_of_names[counter] = name
            counter += 1

    return list_of_names


print(
    "============================================== \nProgram to generate names. v1.1 "
    "\n==============================================")
print(gen_name())
