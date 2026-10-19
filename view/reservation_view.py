import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox


class ReservationView:
    def __init__(
        self,
        root,
        reservation_controller,
        room_controller,
        guest_controller
    ):
        self.reservation_controller = reservation_controller
        self.room_controller = room_controller
        self.guest_controller = guest_controller

        self.rooms = self.room_controller.find_all_room()
        self.guests = self.guest_controller.find_all_guest()

        self.window = tk.Toplevel(root)
        self.window.title("Add Reservation")
        self.window.geometry("380x420")

        self.reservation_id_entry = self.add_entry("Reservation ID:")

        ttk.Label(self.window, text="Room:").pack(anchor="w", padx=15)
        self.room_combo = ttk.Combobox(
            self.window,
            values=[str(room.room_number) for room in self.rooms],
            state="readonly"
        )
        self.room_combo.pack(fill="x", padx=15, pady=(0, 8))

        ttk.Label(self.window, text="Guest:").pack(anchor="w", padx=15)
        self.guest_combo = ttk.Combobox(
            self.window,
            values=[guest.national_id for guest in self.guests],
            state="readonly"
        )
        self.guest_combo.pack(fill="x", padx=15, pady=(0, 8))

        self.check_in_entry = self.add_entry("Check-in date (YYYY-MM-DD):")
        self.check_out_entry = self.add_entry("Check-out date (YYYY-MM-DD):")
        self.guest_count_entry = self.add_entry("Guest count:")

        ttk.Button(
            self.window,
            text="Save reservation",
            command=self.save_reservation
        ).pack(pady=12)

    def add_entry(self, label_text):
        ttk.Label(self.window, text=label_text).pack(anchor="w", padx=15)
        entry = ttk.Entry(self.window)
        entry.pack(fill="x", padx=15, pady=(0, 8))
        return entry

    def save_reservation(self):
        try:
            room_number = int(self.room_combo.get())
            national_id = self.guest_combo.get()

            room = self.room_controller.find_by_room_number(room_number)
            guest = self.guest_controller.find_by_national_id(national_id)

            result = self.reservation_controller.save(
                reservation_id=int(self.reservation_id_entry.get()),
                booking_date=date.today(),
                check_in_date=date.fromisoformat(self.check_in_entry.get()),
                check_out_date=date.fromisoformat(self.check_out_entry.get()),
                guest_count=int(self.guest_count_entry.get()),
                reservation_status="confirmed",
                room=room,
                guest=guest
            )

            if result == "Reservation saved successfully.":
                messagebox.showinfo("Reservation", result)
            else:
                messagebox.showerror("Reservation", result)

        except ValueError:
            messagebox.showerror(
                "Reservation",
                "Check the ID, dates, and guest count. Dates must use YYYY-MM-DD."
            )