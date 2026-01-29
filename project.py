# Make a class called, “Restaurant”. 
# The __init__() method for Restaurant should store two attributes: 
# Restaurant_name & Cuisine_type.

class Restaurant():
    def __init__(self, Restaurant_name, Cuisine_type):
        self.name = Restaurant_name
        self.cusine = Cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.name}")
        print(f"Restaurant cuisine is {self.cusine}")

restaurant1 = Restaurant('Akbars', 'Pakistani')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Mr Sue', 'Chinese')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Five Guys', 'American')
restaurant3.describe_restaurant()

