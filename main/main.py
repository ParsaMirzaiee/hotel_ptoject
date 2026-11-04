import tkinter as tk
from tkinter import ttk

from controller.guest_controller import GuestController
from controller.reservation_controller import ReservationController
from controller.room_controller import RoomController

from view.guest_view import GuestView
from view.reservation_view import ReservationView
from view.room_view import RoomView

root = tk.Tk()
root.title("Hotel Reservation System")
root.geometry("420x380")
root.configure(bg="#F3F6FA")
root.resizable(False, False)

# ظاهر مشترک اجزای ttk
style = ttk.Style(root)
style.theme_use("clam")

style.configure(
    "TButton",
    background="#2878B5",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=(12, 8)
)

style.map(
    "TButton",
    background=[("active", "#1D5F91")]
)

style.configure(
    "TEntry",
    padding=7
)

style.configure(
    "TCombobox",
    padding=7
)

# هر کنترلر فقط یک بار ساخته می‌شود
room_controller = RoomController()
guest_controller = GuestController()
reservation_controller = ReservationController()

# عنوان پنجرهٔ اصلی
tk.Label(
    root,
    text="Hotel Reservation",
    bg="#F3F6FA",
    fg="#243247",
    font=("Segoe UI", 20, "bold")
).pack(pady=(35, 8))

tk.Label(
    root,
    text="Choose a step to continue",
    bg="#F3F6FA",
    fg="#617187",
    font=("Segoe UI", 10)
).pack(pady=(0, 22))

# دکمه‌های باز کردن فرم‌ها
ttk.Button(
    root,
    text="1. Add Room",
    command=lambda: RoomView(root, room_controller)
).pack(fill="x", padx=70, pady=6)

ttk.Button(
    root,
    text="2. Add Guest",
    command=lambda: GuestView(root, guest_controller)
).pack(fill="x", padx=70, pady=6)

ttk.Button(
    root,
    text="3. Add Reservation",
    command=lambda: ReservationView(
        root,
        reservation_controller,
        room_controller,
        guest_controller
    )
).pack(fill="x", padx=70, pady=6)

root.mainloop()
