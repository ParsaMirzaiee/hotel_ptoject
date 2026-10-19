from business_logic.reservation_bl import ReservationBL
from model.reservation import Reservation


class ReservationController:
    def __init__(self):
        self.reservation_bl = ReservationBL()

    def save(
        self,
        reservation_id,
        booking_date,
        check_in_date,
        check_out_date,
        guest_count,
        reservation_status,
        room,
        guest
    ):
        try:
            reservation = Reservation(
                reservation_id,
                booking_date,
                check_in_date,
                check_out_date,
                guest_count,
                reservation_status,
                room,
                guest
            )

            self.reservation_bl.save(reservation)
            return "Reservation saved successfully."


        except Exception as error:

            return f"Operation failed: {error}"


    def find_all_reservations(self):
        return self.reservation_bl.find_all_reservations()

    def cancel(self, reservation_id):
        try:
            self.reservation_bl.cancel(reservation_id)
            return "Reservation cancelled successfully."


        except Exception as error:

            return f"Operation failed: {error}"