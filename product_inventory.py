#!/usr/bin/python3
# product_inventory.py Prakash Acharya
products = []  # list to hold all the product objects


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price  # price per item
        self.quantity = quantity
        products.append(self)


class Inventory:
    def __init__(self, name="main inventory"):
        self.name = name

    def calculate_sum(self):
        summation = 0
        for item in products:
            summation += (item.price * item.quantity)
        return summation

    def items_status(self):
        print("Following is what we have in {inventory}:"
              .format(inventory=self.name))
        print("\nITEM".ljust(30), "QUANTITY".ljust(20))
        for item in products:
            print(item.name.ljust(30), str(item.quantity).ljust(20))


# adding three new product objects
soap = Product('Imperial Leather soap', price=29, quantity=100)
biscuit = Product('Digestive biscuit', price=20, quantity=60)
brush = Product("Oral B brush", price=65, quantity=20)

# adding new inventory object
kotkantie_inventory = Inventory('Kotkantie Inventory')
print("Total inventory value: " + str(kotkantie_inventory.calculate_sum()))

# print items and their availability in the inventory
kotkantie_inventory.items_status()
