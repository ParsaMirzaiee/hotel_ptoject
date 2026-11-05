from data_access.reservation_da import ReservationDA


class ReservationBL:
    def __init__(self):
        self.reservation_da = ReservationDA()

    def get_next_reservation_id(self):
        reservations = self.reservation_da.find_all_reservations()
        next_id = 1

        for reservation in reservations:
            if reservation.reservation_id >= next_id:
                next_id = reservation.reservation_id + 1

        return next_id

    def find_available_room(
            self,
            rooms,
            check_in_date,
            check_out_date,
            guest_count,
            has_view
    ):
        selected_room = None

        for room in rooms:
            if (
                    room.status == "available"
                    and room.capacity >= guest_count
                    and room.has_view == has_view
            ):
                room_is_available = True

                room_reservations = self.reservation_da.find_by_room_number(
                    room.room_number
                )

                for existing in room_reservations:
                    if existing.reservation_status != "cancelled":
                        dates_overlap = (
                                check_in_date < existing.check_out_date
                                and check_out_date > existing.check_in_date
                        )

                        if dates_overlap:
                            room_is_available = False
                            break

                if room_is_available:
                    if (
                            selected_room is None
                            or room.capacity < selected_room.capacity
                    ):
                        selected_room = room

        return selected_room





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