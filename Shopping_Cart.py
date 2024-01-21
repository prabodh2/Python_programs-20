# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def addItem(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def removeItem(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity

    def calcTotal(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total


cart = ShoppingCart()

cart.addItem("Laptop", 1000)
cart.addItem("Headphones", 50, 2)
cart.addItem("Mouse", 20)

total_price = cart.calcTotal()
print(f"Total Price: ₹{total_price}")

cart.removeItem("Headphones", 1)

updated_total_price = cart.calcTotal()
print(f"Updated Total Price: ₹{updated_total_price}")
