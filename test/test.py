from datetime import date
#تست مشتریان
# customer1 = Guest("0110226534",
#                   "parsa",
#                   "mirzaie",
#                   date(2003,2,7),
#                   "24",
#                   "male",
#                   "09129262395"
#                   )

# print(customer1)
# customer2 = Guest("0421816651",
#                   "tara",
#                   "mirzaie",
#                   date(2008,6,12),
#                   "20",
#                   "female",
#                   "")
#
# print(customer2)
# ----------------------------------------------------------------------------------------------------
import tkinter as tk

from controller.room_controller import RoomController
from view.room_view import RoomView


root = tk.Tk()
root.withdraw()

room_controller = RoomController()
RoomView(root, room_controller)

root.mainloop()
#===========================================================================================
# import tkinter as tk
#
# from controller.guest_controller import GuestController
# from view.guest_view import GuestView
#
#
# root = tk.Tk()
# root.withdraw()
#
# guest_controller = GuestController()
# GuestView(root, guest_controller)
#
# root.mainloop()

#===================================================================================================
# import tkinter as tk
# from datetime import date, timedelta
#
# from controller.guest_controller import GuestController
# from controller.reservation_controller import ReservationController
# from controller.room_controller import RoomController
# from view.reservation_view import ReservationView
#
#
# root = tk.Tk()
# root.withdraw()
#
# room_controller = RoomController()
# guest_controller = GuestController()
# reservation_controller = ReservationController()
#
# room_controller.save(
#     room_number=101,
#     capacity=2,
#     bed_configuration="1 double bed",
#     price_per_night=500000,
#     has_view=False,
#     status="available"
# )
#
# guest_controller.save(
#     national_id="1234567890",
#     first_name="Ali",
#     last_name="Ahmadi",
#     birthdate=date(2000, 5, 12),
#     gender="male",
#     phone_number="09123456789"
# )
#
# check_in = date.today() + timedelta(days=3)
# check_out = check_in + timedelta(days=2)
#
# print("For a valid reservation, enter these dates:")
# print("Check-in:", check_in)
# print("Check-out:", check_out)
#
# ReservationView(
#     root,
#     reservation_controller,
#     room_controller,
#     guest_controller
# )
#
# root.mainloop()