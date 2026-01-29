import tkinter as tk
from tkinter import messagebox, simpledialog
from dataclasses import dataclass
from typing import Dict, List

TEAM_NAME = "Brew & Bound"
EMPLOYEE_PASSWORD = "letmein"


# ---------- Data Models ----------
@dataclass
class Product:
    id: str
    category: str
    name: str
    price: float
    stock: int
    details: str
    delivery_eligible: bool = False


@dataclass
class BasketItem:
    product_id: str
    name: str
    unit_price: float
    qty: int


# ---------- Inventory ----------
def seed_inventory() -> Dict[str, Product]:
    return {
        "D1": Product("D1", "drinks", "Flat White", 3.60, 30, "Espresso + milk"),
        "D2": Product("D2", "drinks", "Matcha Latte", 4.10, 20, "Matcha + milk"),
        "F1": Product("F1", "food", "Brownie", 2.90, 15, "Chocolate brownie"),
        "F2": Product("F2", "food", "Carrot Cake", 3.40, 10, "Carrot & cinnamon"),
        "B1": Product("B1", "books", "Atomic Habits", 12.99, 8, "James Clear", True),
        "B2": Product("B2", "books", "Deep Work", 11.50, 5, "Cal Newport", True),
    }


# ---------- GUI App ----------
class BrewBoundApp:
    def __init__(self, root):
        self.root = root
        self.root.title(TEAM_NAME)

        self.inventory = seed_inventory()
        self.basket: List[BasketItem] = []

        self.category = None

        # Layout
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text=TEAM_NAME, font=("Arial", 18, "bold"))
        title.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        for cat in ("drinks", "food", "books"):
            tk.Button(
                btn_frame,
                text=cat.title(),
                width=10,
                command=lambda c=cat: self.show_category(c)
            ).pack(side=tk.LEFT, padx=5)

        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=10)

        tk.Button(self.root, text="Add to Basket", command=self.add_to_basket).pack()
        tk.Button(self.root, text="View Basket", command=self.view_basket).pack(pady=5)
        tk.Button(self.root, text="Checkout", command=self.checkout).pack(pady=5)

    def show_category(self, category):
        self.category = category
        self.listbox.delete(0, tk.END)

        for p in self.inventory.values():
            if p.category == category:
                self.listbox.insert(
                    tk.END,
                    f"{p.id} | {p.name} | £{p.price:.2f} | stock: {p.stock}"
                )

    def add_to_basket(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("Select item", "Please select a product.")
            return

        item_text = self.listbox.get(selection[0])
        pid = item_text.split("|")[0].strip()
        product = self.inventory[pid]

        if product.stock <= 0:
            messagebox.showerror("Out of stock", "This item is out of stock.")
            return

        qty = simpledialog.askinteger(
            "Quantity", f"How many {product.name}?",
            minvalue=1, maxvalue=product.stock
        )

        if not qty:
            return

        product.stock -= qty

        for item in self.basket:
            if item.product_id == pid:
                item.qty += qty
                break
        else:
            self.basket.append(BasketItem(pid, product.name, product.price, qty))

        messagebox.showinfo("Added", "Item added to basket!")
        self.show_category(self.category)

    def view_basket(self):
        if not self.basket:
            messagebox.showinfo("Basket", "Basket is empty.")
            return

        text = ""
        total = 0
        for item in self.basket:
            line = item.unit_price * item.qty
            total += line
            text += f"{item.name} x{item.qty} = £{line:.2f}\n"

        text += f"\nTotal: £{total:.2f}"
        messagebox.showinfo("Your Basket", text)

    def checkout(self):
        if not self.basket:
            messagebox.showwarning("Empty", "Basket is empty.")
            return

        total = sum(i.unit_price * i.qty for i in self.basket)

        if messagebox.askyesno("Employee", "Are you an employee?"):
            pw = simpledialog.askstring("Password", "Enter password:", show="*")
            if pw == EMPLOYEE_PASSWORD:
                total *= 0.9
                messagebox.showinfo("Discount", "10% discount applied!")
            else:
                messagebox.showerror("Error", "Incorrect password")

        if messagebox.askyesno("Confirm", f"Place order for £{total:.2f}?"):
            messagebox.showinfo("Success", "Order placed! ☕📚")
            self.basket.clear()


# ---------- Run ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = BrewBoundApp(root)
    root.mainloop()

