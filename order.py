import os

os.chdir(r'C:\PLD2023')

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def show_order_confirmation(name, age, address, quantity):
    item_price = 84990.00
    taxes_percentage = 0.12
    discount_percentage = 0.05

    subtotal = quantity * item_price
    taxes = subtotal * taxes_percentage
    discount = subtotal * discount_percentage
    total_amount = subtotal + taxes - discount

    formatted_subtotal = f"₱{subtotal:.2f}"
    formatted_taxes = f"₱{taxes:.2f}"
    formatted_discount = f"₱{discount:.2f}"
    formatted_total = f"₱{total_amount:.2f}"

    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    confirmation_message = f"Order Confirmation\n\n"\
                            f"Date: {order_date}\n"\
                            f"Name: {name}\n"\
                            f"Age: {age}\n"\
                            f"Address: {address}\n\n"\
                            f"Item: iPhone 15 Pro Max\n"\
                            f"Quantity: {quantity}\n"\
                            f"Unit Price: ₱{item_price:.2f}\n"\
                            f"Subtotal: {formatted_subtotal}\n"\
                            f"Taxes ({taxes_percentage*100}%): {formatted_taxes}\n"\
                            f"Discount ({discount_percentage*100}%): {formatted_discount}\n"\
                            f"Total Amount: {formatted_total}"

    messagebox.showinfo("Order Confirmation", confirmation_message)

root = tk.Tk()
root.title("Fake Online Shopping")

label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_address = tk.Label(root, text="Address:")
label_address.pack()

entry_address = tk.Entry(root)
entry_address.pack()

label_quantity = tk.Label(root, text="Quantity:")
label_quantity.pack()

entry_quantity = tk.Entry(root)
entry_quantity.pack()

confirm_button = tk.Button(root, text="Confirm Purchase", command=lambda: show_order_confirmation(entry_name.get(), entry_age.get(), entry_address.get(), int(entry_quantity.get())))
confirm_button.pack()

root.mainloop()
