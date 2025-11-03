# Task 1: Shopping Cart System

cart = []  

num_items = int(input("How many products do you want to add? "))

for i in range(num_items):
    name = input(f"Enter name for product {i+1}: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    item = {"name": name, "price": price, "quantity": quantity}
    cart.append(item)

total = 0
print("\n--- Shopping Cart ---")
for item in cart:
    item_total = item["price"] * item["quantity"]
    total += item_total
    print(f"{item['name']}: {item['quantity']} x {item['price']} = {item_total:.2f}")

if total >= 500:
    discount = total * 0.10
    total -= discount
    print(f"\n10% discount applied! Discount amount: {discount:.2f}")

print(f"Final Total: {total:.2f}")
