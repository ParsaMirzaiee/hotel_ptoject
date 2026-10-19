from data_access.reservation_da import ReservationDA


class ReservationBL:
    def __init__(self):
        self.reservation_da = ReservationDA()

    def save(self, reservation):
        if reservation.check_out_date <= reservation.check_in_date:
            raise ValueError("Check-out date must be after check-in date.")

        if reservation.guest_count > reservation.room.capacity:
            raise ValueError("Guest count exceeds room capacity.")

        if reservation.room.status != "available":
            raise ValueError("This room cannot be reserved.")

        existing_reservation = self.reservation_da.find_by_reservation_id(
            reservation.reservation_id
        )

        if existing_reservation is not None:
            raise ValueError("This reservation ID already exists.")

        room_reservations = self.reservation_da.find_by_room_number(
            reservation.room.room_number
        )

        for existing_reservation in room_reservations:
            if existing_reservation.reservation_status == "cancelled":
                continue

            dates_overlap = (
                reservation.check_in_date < existing_reservation.check_out_date
                and reservation.check_out_date > existing_reservation.check_in_date
            )

            if dates_overlap:
                raise ValueError(
                    "This room is already reserved for these dates."
                )

        self.reservation_da.save(reservation)

    def find_all_reservations(self):
        return self.reservation_da.find_all_reservations()

    def cancel(self, reservation_id):
        reservation = self.reservation_da.find_by_reservation_id(reservation_id)

        if reservation is None:
            raise ValueError("Reservation was not found.")

        reservation.cancel()