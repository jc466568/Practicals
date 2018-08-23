
# for i in range(0, 150, 50):
#     print("{0:>3}".format(i))

river = 'Jordan'
target = input('Input: ')
for index, letter in enumerate(river):
    if letter == target:
        print("Letter found at: ", index)
        break
else:
    print('Letter', target, 'not found in', river)