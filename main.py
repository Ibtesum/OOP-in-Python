class Item:
    # Any methods starting and ending with double underscore is called Magic/Dunder methods
    def __init__(self, name, price , quantity=0) -> None: # __init__ returns None type
        self.name = name # Assigning dynamic attribute
        self.price = price # Assigning dynamic attribute
        self.quantity = quantity # Assigning dynamic attribute
    def calculate_total_price(self):
        return f'Total price for {self.name} is: {self.price * self.quantity}' 

# Instance of the Item class
item1 = Item("Phone", 100, 3)
# Another Instance of the Item class
item2 = Item("Laptop", 5000, 5)

print(item1.name)
print(item1.price)
print(item1.quantity)

print(item2.name)
print(item2.price)
print(item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

