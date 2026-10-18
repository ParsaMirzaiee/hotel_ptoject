from tools.validation import *

class Reservation:
    def __init__(self, reservation_id,
                 booking_date,
                 check_in_date,
                 check_out_date,
                 guest_count,
                 reservation_status,
                 room,
                 guest
                 ):
        self.reservation_id = reservation_id
        self.booking_date = booking_date
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.guest_count = guest_count
        self.reservation_status = reservation_status
        self.room = room
        self.guest = guest

    @property
    def reservation_id(self):
        return self.__reservation_id

    @reservation_id.setter
    def reservation_id(self, reservation_id):
        reservation_id_validator(reservation_id)
        self.__reservation_id = reservation_id

    @property
    def booking_date(self):
        return self.__booking_date

    @booking_date.setter
    def booking_date(self, booking_date):
        booking_date_validator(booking_date)
        self.__booking_date = booking_date

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        check_in_date_validator(check_in_date)
        self.__check_in_date = check_in_date

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        check_out_date_validator(check_out_date)
        self.__check_out_date = check_out_date

    @property
    def guest_count(self):
        return self.__guest_count

    @guest_count.setter
    def guest_count(self, guest_count):
        guest_count_validator(guest_count)
        self.__guest_count = guest_count

    @property
    def reservation_status(self):
        return self.__reservation_status

    @reservation_status.setter
    def reservation_status(self, reservation_status):
        reservation_status_validator(reservation_status)
        self.__reservation_status = reservation_status

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, room):
        self.__room = room

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, guest):
        self.__guest = guest