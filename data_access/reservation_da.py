class ReservationDA:
    def __init__(self):
        self.reservations_list = []


    def save(self, reservation):
        self.reservations_list.append(reservation)


    def find_by_room_number(self, room_number):
        result = []

        for reservation in self.reservations_list:
            if reservation.room.room_number == room_number:
                result.append(reservation)

        return result

    def find_by_reservation_id(self, reservation_id):
        for reservation in self.reservations_list:
            if reservation.reservation_id == reservation_id:
                return reservation

        return None


    def find_all_reservations(self):
        return self.reservations_list





