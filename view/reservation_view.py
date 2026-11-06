import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox

from view.payment_view import PaymentView


class ReservationView:
    def __init__(
        self,
        root,
        reservation_controller,
        room_controller,
        guest,
        payment_controller
    ):
        self.root = root
        self.reservation_controller = reservation_controller
        self.room_controller = room_controller
        self.payment_controller = payment_controller
        self.guest = guest

        self.window = tk.Toplevel(root)
        self.window.title("Reservation Information")
        self.window.geometry("380x350")

        ttk.Label(
            self.window,
            text=f"Guest: {self.guest.first_name} {self.guest.last_name}"
        ).pack(anchor="w", padx=15, pady=(15, 8))

        ttk.Label(self.window, text="Room view:").pack(
            anchor="w",
            padx=15
        )

        self.has_view_combo = ttk.Combobox(
            self.window,
            values=["No", "Yes"],
            state="readonly"
        )
        self.has_view_combo.current(0)
        self.has_view_combo.pack(fill="x", padx=15, pady=(0, 8))

        self.check_in_entry = self.add_entry(
            "Check-in date (YYYY-MM-DD):"
        )
        self.check_out_entry = self.add_entry(
            "Check-out date (YYYY-MM-DD):"
        )
        self.guest_count_entry = self.add_entry("Guest count:")

        ttk.Button(
            self.window,
            text="Save reservation",
            command=self.save_reservation
        ).pack(pady=12)

    def add_entry(self, label_text):
        ttk.Label(
            self.window,
            text=label_text
        ).pack(anchor="w", padx=15)

        entry = ttk.Entry(self.window)
        entry.pack(fill="x", padx=15, pady=(0, 8))
        return entry

    def save_reservation(self):
        try:
            result = self.reservation_controller.save(
                booking_date=date.today(),
                check_in_date=date.fromisoformat(
                    self.check_in_entry.get()
                ),
                check_out_date=date.fromisoformat(
                    self.check_out_entry.get()
                ),
                guest_count=int(self.guest_count_entry.get()),
                has_view=self.has_view_combo.get() == "Yes",
                reservation_status="confirmed",
                rooms=self.room_controller.find_all_room(),
                guest=self.guest
            )

            if result.startswith("Reservation saved successfully."):
                messagebox.showinfo("Reservation", result)

                reservations = (
                    self.reservation_controller.find_all_reservations()
                )
                reservation = reservations[-1]

                PaymentView(
                    self.root,
                    self.payment_controller,
                    reservation
                )
            else:
                messagebox.showerror("Reservation", result)

        except ValueError as error:
            messagebox.showerror(
                "Reservation",
                f"Check the dates and guest count. {error}"
            )