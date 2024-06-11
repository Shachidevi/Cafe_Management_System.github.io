import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class CafeManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Cafe Management System")
        self.root.geometry("650x500")
        self.root.configure(bg='lightblue')

        self.menu_items = {
            "Coffee": 10.00,
            "Tea": 20.00,
            "Sandwich": 60.00,
            "Cake": 30.00,
            "Juice": 50.00,
            "Cookie":10.00
        }

        self.orders = []

        self.create_widgets()

        lblHeading =tk.Label(root,text = 'Cafe Management System', bg='blue', fg='white', font=('Impact',24))
        lblHeading.place(x=160,y=20)

    def create_widgets(self):
        # Menu Items
        
        self.menu_label = tk.Label(self.root, text="Menu Items", font=("Helvetica", 16, "bold"))
        self.menu_label.place(x=50, y=80)

        self.menu_listbox = tk.Listbox(self.root, width=25, height=6, font=(12))
        self.menu_listbox.place(x=30, y=120)

        for item in self.menu_items:
            self.menu_listbox.insert(tk.END, f"{item}:  ₹:{self.menu_items[item]:.2f}")

        # Order Section
        self.order_label = tk.Label(self.root, text="Place Your Order", font=("Helvetica", 16, "bold"))
        self.order_label.place(x=350, y=80)

        self.order_var = tk.StringVar()
        self.order_entry = tk.Entry(self.root, textvariable=self.order_var, width=30)
        self.order_entry.place(x=350, y=120)

        self.add_to_order_btn = tk.Button(self.root, text="Add to Order", command=self.add_to_order)
        self.add_to_order_btn.place(x=400, y=150)

        # Order List
        self.order_listbox = tk.Listbox(self.root, width=40, height=10)
        self.order_listbox.place(x=320, y=180)

        # Total Cost
        self.total_label = tk.Label(self.root, text="Total Cost:", font=("Helvetica", 14))
        self.total_label.place(x=200, y=350)

        self.total_var = tk.StringVar()
        self.total_var.set("₹0.00")
        self.total_amount_label = tk.Label(self.root, textvariable=self.total_var, font=("Helvetica", 14))
        self.total_amount_label.place(x=320, y=350)

        # Checkout Button
        self.checkout_btn = tk.Button(self.root, text="Generate Bill", command=self.checkout)
        self.checkout_btn.place(x=260, y=400)

    def add_to_order(self):
        order_item = self.order_var.get().strip()
        if order_item in self.menu_items:
            self.orders.append((order_item, self.menu_items[order_item]))
            self.update_order_listbox()
            self.update_total_cost()
        else:
            messagebox.showerror("Error", "Invalid menu item")

    def update_order_listbox(self):
        self.order_listbox.delete(0, tk.END)
        for item, price in self.orders:
            self.order_listbox.insert(tk.END, f"{item}: ₹{price:.2f}")

    def update_total_cost(self):
        total_cost = sum(price for _, price in self.orders)
        self.total_var.set(f"₹{total_cost:.2f}")

    def checkout(self):
        total_cost = sum(price for _, price in self.orders)
        bill = self.generate_bill(total_cost)
        self.save_bill(bill)
        messagebox.showinfo("Generate Bill", bill)
        self.orders = []
        self.update_order_listbox()
        self.update_total_cost()

    def generate_bill(self, total_cost):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        bill = "-----------------------------\n"
        bill += "          CAFE BILL\n"
        bill += "-----------------------------\n"
        for item, price in self.orders:
            bill += f"{item}: Rs:{price:.2f}\n"
        bill += "-----------------------------\n"
        bill += f"Total: Rs:{total_cost:.2f}\n"
        bill += "-----------------------------"
        return bill

    def save_bill(self, bill):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"cafe_bill_{timestamp}.txt"
        with open(file_name, "w") as file:
            file.write(bill)

if __name__ == "__main__":
    root = tk.Tk()
    app = CafeManagementSystem(root)
    root.mainloop()
