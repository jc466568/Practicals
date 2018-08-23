#
# name = input("Enter your name: ")
# out_file = open('{}.txt'.format(name), 'w')  # file for writing outputs
# print("Your name is", name, file=out_file)
# out_file.close()
#
# out_file = open('{}.txt'.format(name), 'r')  # file for reading outputs
# read_file = out_file.read()
# print(read_file)
# out_file.close()

out_file = open('number.txt', 'w')
print('17', '\n', '42', sep="", file=out_file)
out_file.close()

out_file = open('number.txt', 'r')
total = 0
for line in out_file:
    number = int(line)
    total += number
print(total)
