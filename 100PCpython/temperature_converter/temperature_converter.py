"""
Program to convert temperature to different scales.

By Gabriel Cavalcante
"""

# Main function


def temp_conv():
    print("=========================================================\n" +
          "Program to convert temperatures to different scales by Gabriel Cavalcante\n" +
          ":")

    # Variable do decide if the program continues to operate or not.
    close = False
    while not close:
        scale = input(
            "Select the desired scale:\n(c) for Celsius.\n(k) for Kelvin.\n(f) for Fahrenheit.\n-> ").lower()
        temperature = float(input("Type the degree in {}: ".format(scale)))

        # If the scale is Celsius
        if scale == "c":
            fromCelsius(temperature)
        # If the scale is Kelvin
        elif scale == "k":
            fromKelvin(temperature)

        # If the scale is Fahrenheit
        elif scale == "f":
            fromFahrenheit(temperature)

        # Asks if the user wishes to continue to operate the program
        closure = input(
            "Do you wish to continue to convert temperatures?('y' or 'n'): ").lower()
        # If the answer is no
        if closure == "n":
            close = True  # Program ends in this condition
            print("End of the program.")


# Function for the Celsius conversion
def fromCelsius(temp):
    '''
    This function triggers if the user chooses to convert the temperature from Celsius.
    It takes an entry (temp) and asks to what scale the user wishes to convert to.
    '''
    opt = input(
        "What do you wish to convert it to:\n(k) for Kelvin.\n(f) for Fahrenheit.\n-> ").lower()
    if opt == "k":
        celsiusToKelvin(temp)
    if opt == "f":
        celsiusToFahrenheit(temp)

# Function for the Kelvin conversion


def fromKelvin(temp):
    '''
    This function triggers if the user chooses to convert the temperature from Kelvin.
    It takes an entry (temp) and asks to what scale the user wishes to convert to.
    '''
    opt = input(
        "What do you wish to convert to:\n(c) for Celsius.\n(f) for Fahrenheit.\n-> ").lower()
    if opt == "c":
        kelvinToCelsius(temp)
    if opt == "f":
        kelvinToFahrenheit(temp)

# Function for the Fahrenheit conversion


def fromFahrenheit(temp):
    '''
    This function triggers if the user chooses to convert the temperature from Fahrenheit.
    It takes an entry (temp) and asks to what scale the user wishes to convert to.
    '''
    opt = input(
        "What do you wish to convert to:\n(c) for Celsius.\n(k) for Kelvin.\n-> ").lower()
    if opt == "c":
        fahrenheitToCelsius(temp)
    if opt == "k":
        fahrenheitToKelvin(temp)


# Function to calculate the conversion from Celsius to Kelvin
def celsiusToKelvin(temp):
    '''
    This function calculates the conversion from Celsius to Kelvin.
    '''
    print("{}ºC para Kelvin: ".format(temp))
    c_to_k = float(temp + 273.15)
    print(c_to_k)

# Function to calculate the conversion from Celsius to Fahrenheit


def celsiusToFahrenheit(temp):
    '''
    This function calculates the conversion from Celsius to Fahrenheit.
    '''
    print("{}ºC para Fahrenheit: ".format(temp))
    c_to_f = float((1.8*temp) + 32)
    print(c_to_f)

# Function to calculate the conversion from Kelvin to Fahrenheit


def kelvinToFahrenheit(temp):
    '''
    This function calculates the conversion from Kelvin to Fahrenheit.
    '''
    print("{}ºK para Fahrenheit: ".format(temperature))
    k_to_f = float(1.8 * (temperature - 273) + 32)
    print("{}ºF".format(k_to_f))

# Function to calculate the conversion from Kelvin to Celsius


def kelvinToCelsius(temp):
    '''
    This function calculates the conversion from Kelvin to Celsius.
    '''
    print("{}ºK para Celsius: ".format(temp))
    k_to_c = float(temp - 273.15)
    print("{}ºC".format(k_to_c))

# Function to calculate the conversion from Fahrenheit to Celsius


def fahrenheitToCelsius(temp):
    '''
    This function calculates the conversion from Fahrenheit to Celsius.
    '''
    print("{}ºF para Celsius: ".format(temperature))
    f_to_c = float((temperature-32)/1.8)
    print("{}ºC".format(f_to_c))

# Function to calculate the conversion from Fahrenheit to Kelvin


def fahrenheitToKelvin(temp):
    '''
    This function calculates the conversion from Fahrenheit to Kelvin.
    '''
    print("{}ºF para Kelvin: ".format(temp))
    f_to_k = float((temp + 459.67)*(5/9))
    print("{}ºK".format(f_to_k))


# Initiates the program
temp_conv()
