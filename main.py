class Item:
    pay_rate = 0.8 # Class Attribute. For a 20% discount.

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
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate # Here, we can also write Item.pay_rate. But it won't work if we want to change the pay_rate for any specific instance of the Item Class. So, it's a good idea to access pay_rate from instance level. So that we can reassign it.


# Instance of the Item class
item1 = Item("Phone", 100, 3)
# Another Instance of the Item class
item2 = Item("Laptop", 1000, 5)

print(Item.pay_rate) # 0.8

# At first, Instance item1 tries to bring the attribute from instance level, i.e. from the __init__ method. If its not there then it brings from the class level.
print(item1.pay_rate) # 0.8 


# At first, Instance item2 tries to bring the attribute from instance level, i.e. from the __init__ method. If its not there then it brings from the class level.
print(item2.pay_rate) # 0.8



# The __dict__ in Python represents a dictionary or any mapping object that is used to store the attributes of the object. They are also known as mappingproxy objects. To put it simply, every object in Python has an attribute that is denoted by __dict__.
# __dict__ is also called magic attribute, not magic method.

# All attributes for Class level
print(Item.__dict__) # gives pay_rate along with many other things.

# All attributes for Instance level
print(item1.__dict__) # {'name': 'Phone', 'price': 100, 'quantity': 3}


item1.apply_discount()
print(item1.price)  # 80.0


item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price) # 700.0

# These are not necessary for this topic. 
# print(item1.name)
# print(item1.price)
# print(item1.quantity)

# print(item2.name)
# print(item2.price)
# print(item2.quantity)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())



