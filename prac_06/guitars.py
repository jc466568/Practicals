
from prac_06.guitar import Guitar

print("My guitars!")
name = input("Name: ")
guitars = []
guitars_status = []
while name != "":
        year = int(input("Year: "))
        cost = input("Cost: $")
        guitar = Guitar(name, year, cost)
        if guitar.is_vintage():
            status = "(vintage)"
        else:
            status = ""
        guitars_status.append(status)
        guitars.append(guitar)
        print("{} ({}) : ${} added".format(name, year, cost))
        name = input("Name: ")
print("These are my guitars")
n = 1
for i in range(len(guitars)):
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(n, guitar.name, guitar.year, guitar.cost,
                                                              guitars_status[n-1]))
    n += 1
