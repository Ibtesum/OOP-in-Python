class Item:
    # Any methods starting and ending with double underscore is called Magic/Dunder methods
    def __init__(self, name : str, price : float , quantity=0) -> None:
        # We specified the acceptable data types for each received arguments.
        # name accepts string type.
        # price accepts float type but also int type.
        # quantity accepts float and int by default for assigning the default value 0.

        # Run Validation for received arguments
        assert price >= 0, f"Price: {price} cannot be less than 0"
        assert quantity >= 0, f"Quantity: {quantity} cannot be less than 0"
        # The above code creates AssertionError with the message written in formatted string if the instance doesn't fullfill the requirements.

        # Assign Values To self Object
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

