
x = int(input("Enter the minimum value: "))
y = int(input("Enter the maximum value: "))

MENU = """A - Find the even numbers
B - Find the odd numbers
C - Calculate the square of the numbers
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "A":
        even_numbers = []
        for i in range(x, y, 1):
            if i % 2 == 0:
                even_numbers.append(i)
        print(even_numbers)
    elif choice == "B":
        odd_numbers = []
        for i in range(x, y, 1):
            if i % 2 == 1:
                odd_numbers.append(i)
        print(odd_numbers)
    elif choice == "C":
        squares = []
        for i in range(x, y, 1):
            squares.append(i ** 2)
        print(squares)
    else:
        print("Invalid option")
    print(MENU)
    x = int(input("Enter the minimum value: "))
    y = int(input("Enter the maximum value: "))
    choice = input(">>> ").upper()
print("Thank you.")
