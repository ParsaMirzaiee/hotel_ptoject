import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox

from view.reservation_view import ReservationView


class GuestView:
    def __init__(
        self,
        root,
        guest_controller,
        room_controller,
        reservation_controller,
        payment_controller
    ):
        self.root = root
        self.guest_controller = guest_controller
        self.room_controller = room_controller
        self.reservation_controller = reservation_controller
        self.payment_controller = payment_controller

        self.window = tk.Toplevel(root)
        self.window.title("Guest Information")
        self.window.geometry("350x400")

        self.national_id_entry = self.add_entry("National ID:")
        self.first_name_entry = self.add_entry("First name:")
        self.last_name_entry = self.add_entry("Last name:")
        self.birthdate_entry = self.add_entry("Birthdate (YYYY-MM-DD):")

        ttk.Label(self.window, text="Gender:").pack(
            anchor="w",
            padx=15
        )

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
        ).pack(pady=(12, 6))

        self.next_button = ttk.Button(
            self.window,
            text="Next: Reservation Information",
            command=self.open_reservation_view,
            state="disabled"
        )
        self.next_button.pack(pady=6)

    def add_entry(self, label_text):
        ttk.Label(
            self.window,
            text=label_text
        ).pack(anchor="w", padx=15)

        entry = ttk.Entry(self.window)
        entry.pack(fill="x", padx=15, pady=(0, 8))
        return entry

    def save_guest(self):
        try:
            birthdate = date.fromisoformat(
                self.birthdate_entry.get()
            )

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
                self.next_button.config(state="normal")
            else:
                messagebox.showerror("Guest", result)

        except ValueError:
            messagebox.showerror(
                "Guest",
                "Enter the birthdate in YYYY-MM-DD format."
            )

    def open_reservation_view(self):
        guest = self.guest_controller.find_by_national_id(
            self.national_id_entry.get()
        )

        if guest is None:
            messagebox.showerror(
                "Guest",
                "The guest could not be found."
            )
            return

        ReservationView(
            self.root,
            self.reservation_controller,
            self.room_controller,
            guest,
            self.payment_controller
        )