import tkinter as tk
from tkinter import messagebox

from datetime import datetime

def show_confirmation():
    name = entry_name.get()
    age = entry_age.get()
    address = entry_address.get()

    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    confirmation_message =  f"Date: {order_date}\n\n"\
                            f"Thank you, {name}! Your purchase of iPhone 15 Pro Max (256GB) has been confirmed.\n\n"\
                            f"We will deliver your item to:\n{address}\n\n"\
                            f"Please prepare an exact amount of ₱84,990.00 for your payment (Cash On Delivery).\n\n"\
                            f"Estimated delivery time: 3 business days.\n\n"\
                            "Happy shopping!"

    messagebox.showinfo("Order Confirmation", confirmation_message)

root = tk.Tk()
root.title("keme keme")
root.geometry("300x200")

label_name = tk.Label(root, text="Name:")
label_name.pack(padx=5, pady=5)

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack(padx=5, pady=5)

entry_age = tk.Entry(root)
entry_age.pack()

label_address = tk.Label(root, text="Address:")
label_address.pack(padx=5, pady=5)

entry_address = tk.Entry(root)
entry_address.pack()

confirm_button = tk.Button(root, text="Confirm", command=show_confirmation)
confirm_button.pack(padx=5, pady=5)

root.mainloop()