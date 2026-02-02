#here  define the dataclass - this is the manual setting out  rules

from dataclasses import dataclass # from carton of eggs import individual eggs
@dataclass 
class Product:
    id: str
    category: str     #"Drink", #"Food, or "Book"
    name: str  #display name
    price: float #float for decimals
    stock: int  
    details: str  #a short desc for the customer
    delivery_eligible: bool = False
    discount_percent: float = 0.0 #float is best here as discounts can also be decimal. it's 0.0 because unless eligable get no discount

#chuck 2: inventory: the carton showing what exactly is in the product dataclass created

inventory = [
    #drinks
    Product(
        id="D01",
        category="Drink",
        name="Flat White",
        price=3.50,
        stock=20,
        details="Double shot of espresso with cream",
    ),

    Product(
        id="D02",
        category="Drink",
        name="Tea",
        price=3.00,
        stock=10,
        details="English Breakfast Tea",

    ),
    #food
    Product(
        id="F01",
        category="Food",
        name="Lemon Drizzle",
        price=4.00,
        stock=12,
        details="cheesecake",
    ),
    Product(
        id="F02",
        category="Food",
        name="Cookie",
        price=5.00,
        stock=10,
        details="chock chip"

    ),
    #books
    Product(
        id="B01",
        category="Book",
        name="Harry Potter",
        price=10.00,
        stock=12,
        details="Fiction",
        delivery_eligible=True, # overriding the defauls false
    ),

    Product(
        id="B02",
        category="Books",
        name="Atomic Habits",
        price=5.00,
        stock=3,
        details="Self Help",
        delivery_eligible=True, # ovveriding the default false
    )
]
# # Temporary Test
# print("--- Shop Inventory Test ---")
# print(f"Total items in stock: {len(inventory)}")
# print(f"First item: {inventory[0].name}")
# print(f"Last item: {inventory[-1].name}")


#chunk 3 menu display i.e show_menu():

def show_menu():
    # What is displayed
    print ("\n--- Welcome to Paper Cup. Here is our menu ---")
    print(f"{'ID':<6} {'Name':<20} {'Price'}")
    print("-" * 35)
    # \n: Adds a blank line so it doesn't look cramped.

# :<6: found online it tells Python: "Give the ID column 6 spaces of room." 
#it keeps your columns perfectly straight!

# The loop to go through inventory one item at a time

    for item in inventory:
        print(f"{item.id:<6} {item.name:<20} £{item.price:.2f}")
    print("_" * 35)
    #for item in inventory: This says from inventory, get the product id and name 
    # and price and has nicknamed the products item, 
    # and then repeatfor each item (product) until the list is empty.

# :.2f: This is a special rule for floats. found through google suits
#It tells Python: "Always show exactly 2 numbers after the decimal point" 
# (so £3.5 becomes £3.50).

show_menu()

#chunk 4 search engine

# Chunk 4: The Search Engine
def find_product():
    print("\n" + "="*35)
    print("      PRODUCT SEARCH")
    print("="*35)

    # This line tells the computer to WAIT for you to type
    query = input("Enter Product ID (e.g., D01): ").upper().strip()

    found = False
    for item in inventory:
        # Check if what you typed matches the ID in the carton
        if item.id == query:
            print(f"\n[ MATCH FOUND ]")
            print(f"Name:     {item.name}")
            print(f"Category: {item.category}")
            print(f"Details:  {item.details}")
            print(f"Stock:    {item.stock} left")
            print(f"Price:    £{item.price:.2f}")
            found = True
            break # Stop looking once we find it

    if not found:
        print(f"!! No product found with ID: {query} !!")

# Now call it at the very bottom
find_product()
