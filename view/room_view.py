import tkinter as tk
from tkinter import ttk, messagebox


class RoomView:
    bed_configurations = {
        1: "1 single bed",
        2: "1 double bed",
        3: "1 double bed + 1 single bed",
        4: "2 double beds",
        5: "2 double beds + 1 single bed",
    }

    def __init__(self, root, room_controller):
        self.room_controller = room_controller

        self.window = tk.Toplevel(root)
        self.window.title("Add Room")
        self.window.geometry("350x350")

        self.room_number_entry = self.add_entry("Room number:")

        self.capacity_combo = self.add_combo(
            "Capacity:",
            ["1", "2", "3", "4", "5"]
        )
        self.capacity_combo.bind(
            "<<ComboboxSelected>>",
            self.update_bed_configuration
        )

        self.bed_configuration_entry = self.add_entry(
            "Bed configuration:"
        )
        self.bed_configuration_entry.config(state="readonly")

        self.has_view_combo = self.add_combo(
            "Has view:",
            ["True", "False"]
        )

        self.status_combo = self.add_combo(
            "Status:",
            ["available", "unavailable", "maintenance"]
        )

        ttk.Button(
            self.window,
            text="Save room",
            command=self.save_room
        ).pack(pady=12)

    def add_entry(self, label_text):
        ttk.Label(
            self.window,
            text=label_text
        ).pack(anchor="w", padx=15)

        entry = ttk.Entry(self.window)
        entry.pack(fill="x", padx=15, pady=(0, 8))
        return entry

    def add_combo(self, label_text, values):
        ttk.Label(
            self.window,
            text=label_text
        ).pack(anchor="w", padx=15)

        combo = ttk.Combobox(
            self.window,
            values=values,
            state="readonly"
        )
        combo.pack(fill="x", padx=15, pady=(0, 8))
        return combo

    def update_bed_configuration(self, event=None):
        capacity = int(self.capacity_combo.get())
        configuration = self.bed_configurations[capacity]

        self.bed_configuration_entry.config(state="normal")
        self.bed_configuration_entry.delete(0, tk.END)
        self.bed_configuration_entry.insert(0, configuration)
        self.bed_configuration_entry.config(state="readonly")

    def save_room(self):
        try:
            result = self.room_controller.save(
                room_number=int(self.room_number_entry.get()),
                capacity=int(self.capacity_combo.get()),
                bed_configuration=self.bed_configuration_entry.get(),
                has_view=self.has_view_combo.get() == "True",
                status=self.status_combo.get()
            )

            if result == "Room saved successfully.":
                messagebox.showinfo("Room", result)
            else:
                messagebox.showerror("Room", result)

        except ValueError:
            messagebox.showerror(
                "Room",
                "Enter a valid room number and select the room details."
            )