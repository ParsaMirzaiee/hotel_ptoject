import tkinter as tk

from controller.guest_controller import GuestController
from controller.payment_controller import PaymentController
from controller.reservation_controller import ReservationController
from controller.room_controller import RoomController
from view.guest_view import GuestView


root = tk.Tk()
root.withdraw()

room_controller = RoomController()
guest_controller = GuestController()
reservation_controller = ReservationController()
payment_controller = PaymentController()


# موجودی نمونهٔ اتاق‌های هتل
room_controller.save(
    room_number=101,
    capacity=2,
    bed_configuration="1 double bed",
    has_view=False,
    status="available"
)

room_controller.save(
    room_number=102,
    capacity=2,
    bed_configuration="1 double bed",
    has_view=True,
    status="available"
)

room_controller.save(
    room_number=103,
    capacity=3,
    bed_configuration="1 double bed + 1 single bed",
    has_view=False,
    status="available"
)

room_controller.save(
    room_number=104,
    capacity=3,
    bed_configuration="1 double bed + 1 single bed",
    has_view=True,
    status="available"
)

room_controller.save(
    room_number=105,
    capacity=5,
    bed_configuration="2 double beds + 1 single bed",
    has_view=False,
    status="available"
)

room_controller.save(
    room_number=106,
    capacity=5,
    bed_configuration="2 double beds + 1 single bed",
    has_view=True,
    status="available"
)


GuestView(
    root,
    guest_controller,
    room_controller,
    reservation_controller,
    payment_controller
)

root.mainloop()