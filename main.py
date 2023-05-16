class Item:
    pay_rate = 0.8 # Class Attribute. For a 20% discount.
    all = []
    def __init__(self, name : str, price : float , quantity=0) -> None:

        # Run Validation for received arguments
        assert price >= 0, f"Price: {price} cannot be less than 0"
        assert quantity >= 0, f"Quantity: {quantity} cannot be less than 0"
        # The above code creates AssertionError with the message written in formatted string if the instance doesn't fullfill the requirements.

        # Assign Values To self Object
        self.name = name # Assigning dynamic attribute
        self.price = price # Assigning dynamic attribute
        self.quantity = quantity # Assigning dynamic attribute

        # Actions to execute
        Item.all.append(self)
    
    
    # This method is for "representing" the Item class according to our desired way. Without this method print(Item.all) would show the memory address of each instance object.
    def __repr__(self) -> str:
        return f"Item('{self.name}, {self.price}, {self.quantity}')"

    def calculate_total_price(self):
        return f'Total price for {self.name} is: {self.price * self.quantity}' 
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate 
    

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)


print(Item.all)
# Output: [Item('Phone, 100, 1'), Item('Laptop, 1000, 3'), Item('Cable, 10, 5'), Item('Mouse, 50, 5'), Item('Keyboard, 75, 5')]

for instance in Item.all:
    print(instance)
# Output: 
# Item('Phone, 100, 1')
# Item('Laptop, 1000, 3')
# Item('Cable, 10, 5')
# Item('Mouse, 50, 5')
# Item('Keyboard, 75, 5')

