from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

TEAM_NAME = "PaperCup"
EMPLOYEE_PASSWORD = "letmein"

@dataclass
class Product:
    id: str
    category: str  # "drinks" | "food" | "books"
    name: str
    price: float
    stock: int
    details: str  # ingredients / author / description

@dataclass
class BasketItem:
    product_id: str
    name: str
    unit_price: float
    qty: int

def seed_inventory() -> Dict[str, Product]:
    return {
        # Drinks
        "D1": Product("D1", "drinks", "Flat White", 3.60, 30, "Espresso + steamed milk"),
        "D2": Product("D2", "drinks", "Matcha Latte", 4.10, 20, "Matcha + milk"),
        "D3": Product("D3", "drinks", "Iced Americano", 3.20, 25, "Espresso + water + ice"),
        "D4": Product("D4", "drinks", "Tea", 2.00, 10, "Tea + hot water"),  

        # Food (cakes/snacks)
        "F1": Product("F1", "food", "Chocolate Brownie", 2.90, 15, "Cocoa, butter, eggs, sugar, flour"),
        "F2": Product("F2", "food", "Carrot Cake Slice", 3.40, 10, "Carrot, cinnamon, cream cheese frosting"),
        "F3": Product("F3", "food", "Cheese Cake", 4.00, 10, "Cream cheese, digestive, vanilla"),

        # Books
        "B1": Product("B1", "books", "Atomic Habits", 12.99, 8, "James Clear — Habit building"),
        "B2": Product("B2", "books", "The Midnight Library", 9.99, 6, "Matt Haig — Fiction"),
        "B3": Product("B3", "books", "Deep Work", 11.50, 5, "Cal Newport — Focus & productivity"),
        "B4": Product("B3", "books", "Seven Habits of Highly Effective People", 14.99, 7, "Steven Cohen — Habit building"),  
    }
