menu = {
    "Pizza":100,
    "Sdandwich":60,
    "Coffee":50,
    "Burger":65,
    "Pasta":70
}

print("Welcome to Ashu's Restaurant")
print("Pizza:100\nSandwich:60\nCoffe:50\nBurger:65\nPasta:70")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} in not available!")
        
print(f"The total amount of item to pay is {order_total}")                    
