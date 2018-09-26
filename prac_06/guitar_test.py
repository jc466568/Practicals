
from prac_06.guitar import Guitar
import random


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    for i in range(10):
        guitar = Guitar(name, year, cost)
        expected_age = 2018 - year
        print("Age is {}. Expected {}".format(guitar.get_age(), expected_age))
        if expected_age >= 50:
            status = True
        else:
            status = False
        print("Is guitar vintage? {}. Expected {}".format(guitar.is_vintage(), status))
        year = random.randint(1900, 2018)

    # guitar = Guitar(name, year, cost)
    # print(guitar.get_age())
    # print(guitar.is_vintage())
    #
    # name = "Gibson L-5 CES"
    # year = 2000
    # cost = 16035.40
    # guitar = Guitar(name, year, cost)
    # print(guitar.get_age())
    # print(guitar.is_vintage())


main()
