import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox


class GuestView:
    def __init__(self, root, guest_controller):
        self.guest_controller = guest_controller
        self.window = tk.Toplevel(root)
        self.window.title("Add Guest")
        self.window.geometry("350x350")

        self.national_id_entry = self.add_entry("National ID:")
        self.first_name_entry = self.add_entry("First name:")
        self.last_name_entry = self.add_entry("Last name:")
        self.birthdate_entry = self.add_entry("Birthdate (YYYY-MM-DD):")

        ttk.Label(self.window, text="Gender:").pack(anchor="w", padx=15)
        self.gender_combo = ttk.Combobox(
            self.window,
            values=["male", "female"],
            state="readonly"
        )
        self.gender_combo.pack(fill="x", padx=15, pady=(0, 8))

        self.phone_number_entry = self.add_entry("Phone number:")

        ttk.Button(
            self.window,
            text="Save guest",
            command=self.save_guest
        ).pack(pady=12)

    def add_entry(self, label_text):
        ttk.Label(self.window, text=label_text).pack(anchor="w", padx=15)
        entry = ttk.Entry(self.window)
        entry.pack(fill="x", padx=15, pady=(0, 8))
        return entry

    def save_guest(self):
        try:
            birthdate = date.fromisoformat(self.birthdate_entry.get())

            result = self.guest_controller.save(
                national_id=self.national_id_entry.get(),
                first_name=self.first_name_entry.get(),
                last_name=self.last_name_entry.get(),
                birthdate=birthdate,
                gender=self.gender_combo.get(),
                phone_number=self.phone_number_entry.get()
            )

            if result == "Guest saved successfully.":
                messagebox.showinfo("Guest", result)
            else:
                messagebox.showerror("Guest", result)

        except ValueError:
            messagebox.showerror(
                "Guest",
                "Enter the birthdate in YYYY-MM-DD format."
            )