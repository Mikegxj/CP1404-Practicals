total = 0
DISCOUNT = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of Items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total += price_of_item

if total > 0:
    total *= DISCOUNT
print(f"Total price for {number_of_items} items is ${total: .2f}")