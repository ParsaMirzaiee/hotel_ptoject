from datetime import date


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

        if not isinstance(reservation_id,int) or reservation_id<0:
            raise ValueError("reservation_id must be an integer and greater than 0")

        if not isinstance(guest_count,int) or guest_count<0:
            raise ValueError("guest_count must be an integer and greater than 0")

        if check_out_date <= check_in_date:
            raise ValueError("check_out_date must be greater than check_in_date")


        if not isinstance(booking_date,date) or not isinstance(check_in_date,date) or not isinstance(check_out_date,date):
            raise ValueError("booking_date and check_in_date and check_out_date must be of type date")



        self.reservation_id = reservation_id
        self.booking_date = booking_date
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.actual_check_in_time = actual_check_in_time
        self.actual_checkout_time = actual_checkout_time
        self.guest_count = guest_count
        self.status = status


    def calculate_nights(self):
        return (self.check_out_date - self.check_in_date).days

    def calculate_total(self):
        pass

    def cancel_booking(self):
        self.status = "Cancelled"
