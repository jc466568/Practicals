
no_items = int(input("Number of items: "))
total_price = 0

for i in range(no_items):
    item_price = float(input("Enter price: "))
    total_price += item_price
    print("Price of item", i+1, ": ${:.2f}".format(item_price))

print("Number of items: ", no_items)

if total_price > 100:
    total_price = 0.9 * total_price

print("Total price for", no_items, "items is ${:.2f}".format(total_price))
