
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    temperature = float(input("Enter Temperature Value: "))
    if choice == 'C':
        print("Temperature in Fahrenheit is {:.2f} F".format(celsius_to_fahrenheit(temperature)))
    else:
        print("Temperature in Celsius is {:.2f} C".format(fahrenheit_to_celsius(temperature)))


def celsius_to_fahrenheit(temperature):
    return temperature * 9.0 / 5 + 32


def fahrenheit_to_celsius(temperature):
    return 5 / 9 * (temperature - 32)


main()

