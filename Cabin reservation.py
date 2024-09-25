# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:58:51 2023

@author: dylmi
"""

import tkinter as tk
from tkinter import StringVar, messagebox

class CabinReservation:
    def __init__(self, root):
        root.title("Mountain Cabin Resort Reservation")
        
        cabin_type = StringVar()
        view_option = tk.IntVar()
        total_fee = StringVar()

        def calculate_total_fee():
            cabin_types = {"Studio": 500, "One-Bedroom": 700, "Two-Bedroom": 900}
            view_option_fee = 100 if view_option.get() == 1 else 0
            cabin_fee = cabin_types.get(cabin_type.get(), 0)
            total_fee.set(f"Total Fee: ${cabin_fee + view_option_fee}")

        def display_reservation():
            messagebox.showinfo("Reservation Successful", f"Total Fee: {total_fee.get()}")

        tk.Label(root, text="Select Cabin Type:").grid(row=0, column=0, padx=10, pady=10)

        cabin_types = ["Studio", "One-Bedroom", "Two-Bedroom"]
        for i, cabin in enumerate(cabin_types):
            tk.Radiobutton(
                root, text=cabin, variable=cabin_type, value=cabin,
                command=calculate_total_fee
            ).grid(row=1, column=i, padx=5, pady=5)

        tk.Label(root, text="Lake View Option:").grid(row=2, column=0, padx=10, pady=10)
        tk.Checkbutton(
            root, text="Lake View", variable=view_option,
            command=calculate_total_fee
        ).grid(row=3, column=0, padx=5, pady=5)

        tk.Label(root, textvariable=total_fee).grid(row=4, column=0, columnspan=3, pady=10)

        tk.Button(
            root, text="Reserve Cabin", command=display_reservation
        ).grid(row=5, column=0, columnspan=3, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CabinReservation(root)
    root.mainloop()
