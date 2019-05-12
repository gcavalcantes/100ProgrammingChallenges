# Program to convert temperature to different scales


def temp_conv():
    print("=========================================================\n" +
          "Program to convert temperature to different scales by Gabriel Cavalcante\n" +
          ":")
    close = False
    while not close:
        scale = input(
            "Select the desired scale:\n(c) for Celsius.\n(k) for Kelvin.\n(f) for Farenheit.\n-> ").lower()
        temperature = float(input("Type the degree in {}: ".format(scale)))

        # If the scale is Celsius
        if scale == "c":
            opt = input(
                "What do you wish to convert to:\n(k) for Kelvin.\n(f) for Farenheit.\n-> ").lower()
            if opt == "k":
                print("{}ºC para Kelvin: ".format(temperature))
                c_to_k = (temperature + 273.15)
                print(c_to_k)
            if opt == "f":
                print("{}ºC para Farenheit: ".format(temperature))

                print(float((1.8*temperature) + 32))

        # If the scale is Kelvin
        elif scale == "k":
            opt = input(
                "What do you wish to convert to:\n(c) for Celsius.\n(f) for Farenheit.\n-> ")
            if opt == "c":
                print("{}ºK para Celsius: ".format(temperature))
                print("{}ºC".format(float(temperature - 273.15)))
            if opt == "f":
                print("{}ºK para Farenheit: ".format(temperature))
                print("{}ºF".format(float(1.8 * (temperature - 273) + 32)))

        # If the scale is Fahrenheit
        elif scale == "f":
            opt = input(
                "What do you wish to convert to:\n(c) for Celsius.\n(k) for Kelvin.\n-> ")
            if opt == "c":
                print("{}ºF para Celsius: ".format(temperature))
                print("{}ºC".format(float((temperature-32)/1.8)))
            if opt == "k":
                print("{}ºF para Kelvin: ".format(temperature))
                print("{}ºK".format(float((temperature + 459.67)*(5/9))))

        # Asks if the user wishes to continue to operate the program
        closure = input(
            "Do you wish to continue to convert temperatures?('y' or 'n'): ")
        # If the answer is no
        if closure == "n":
            close = True  # Program ends in this condition
            print("End of the program.")


# Initiate the program
temp_conv()
