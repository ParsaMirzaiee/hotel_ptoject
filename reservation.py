class Reservation:
    def __init__(self, reservation_id,
                 booking_date,
                 check_in_date,
                 check_out_date,
                 actual_check_in_time,
                 actual_checkout_time,
                 guest_count,
                 status
                 ):

    @property
    def reservation_id(self):
        return self.__reservation_id
    @reservation_id.setter
    def reservation_id(self,reservation_id):
        # reservation_id_validation(reservation_id)
        self.__reservation_id = reservation_id


    @property
    def booking_date(self):
        return  self.booking_date
    @booking_date.setter
    def booking_date(self,booking_date):
        # booking_date_validation = booking_date
        self.booking_date = booking_date











        self.reservation_id = reservation_id
        self.booking_date = booking_date
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.actual_check_in_time = actual_check_in_time
        self.actual_checkout_time = actual_checkout_time
        self.guest_count = guest_count
        self.status = status



