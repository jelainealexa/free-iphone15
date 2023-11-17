import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def show_confirmation(entry_name, age_combobox, entry_address):
    name = entry_name.get()
    age = age_combobox.get()
    address = entry_address.get()

    if not name or not age or not address:
        messagebox.showwarning("Warning", "Fill this out! Please complete all the fields. 100% Legit!")
        return

    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    confirmation_message = f"Date: {order_date}\n\n"\
                            f"Congratulations, {name}!!! You've just won a FREE iPhone 15 Pro Max (256GB)!\n\n"\
                            f"But wait, there's more! We will personally deliver it to: {address}\n\n"\
                            f"Absolutely no catch! All you need to do is prepare an exact amount of ₱84,990.00 for your payment (Cash On Delivery).\n\n"\
                            f"Estimated time: 3 business seconds!⏰\n\n"\
                            f"For any inquiries, contact our customer support at support@pld2023.com\n\n"\
                            f"Happy shopping! :D"

    messagebox.showinfo("Order Confirmation", confirmation_message)

def start_survey():
    survey_info = "Fill this out to win exciting prizes!!!"

    survey_window = tk.Toplevel(root)
    survey_window.title("Survey")
    survey_window.geometry("300x250")

    label_survey = tk.Label(survey_window, text=survey_info)
    label_survey.pack(pady=3)

    label_name = tk.Label(survey_window, text="Name *")
    label_name.pack(pady=3)

    entry_name = tk.Entry(survey_window)
    entry_name.pack(pady=3)

    label_age = tk.Label(survey_window, text="Age *")
    label_age.pack(pady=3)

    age_combobox = ttk.Combobox(survey_window, values=[str(i) for i in range(1, 80)], state="readonly")
    age_combobox.pack(pady=3)
    age_combobox.set("Select age")

    label_address = tk.Label(survey_window, text="Address *")
    label_address.pack(pady=3)

    entry_address = tk.Entry(survey_window)
    entry_address.pack(pady=3)

    def submit_survey():
        show_confirmation(entry_name, age_combobox, entry_address)
        survey_window.destroy()

    submit_button = tk.Button(survey_window, text="Get Your FREE iPhone 15 NOW!", command=submit_survey, bg="#4CAF50", fg="white")
    submit_button.pack(pady=5)

root = tk.Tk()
root.title("CONGRATULATIONS!")
root.geometry("400x235")

main_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
main_frame.pack(expand=True, fill=tk.BOTH)

header_label = tk.Label(main_frame, text="🌟✨ Checkout - iPhone 15 Pro Max ✨🌟", font=("Helvetica", 16, "bold"))
header_label.pack(pady=(0, 10))

survey_info = f"Today, you have been chosen to participate in this survey.\n"\
                f"We choose 10 random lucky users the chance to win awesome prizes!\n\n"\
                f"You only have 2 minutes to participate!\n"\
                f"Hurry, the number of prizes is limited!!!"

label_survey_info = tk.Label(main_frame, text=survey_info)
label_survey_info.pack(pady=10)

start_survey_button = tk.Button(main_frame, text="Start Survey", command=start_survey, bg="#FFD700")
start_survey_button.pack(pady=10, fill=tk.X)

footer_label = tk.Label(root, text="© 2023 Totally Legit Online Store. All rights reserved. Definitely not a scam!", font=("Helvetica", 8))
footer_label.pack(pady=(10, 0), side=tk.BOTTOM, anchor=tk.CENTER)

root.mainloop()