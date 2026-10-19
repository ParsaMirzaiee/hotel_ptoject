from data_access.room_da import RoomDA


class RoomBL:
    def __init__(self):
        self.room_da = RoomDA()

    def save(self, room):
        existing_room = self.room_da.find_by_room_number(room.room_number)

        if existing_room is not None:
            raise ValueError("This room number already exists.")

        self.room_da.save(room)

    def find_by_room_number(self, room_number):
        return self.room_da.find_by_room_number(room_number)

    def find_all_room(self):
        return self.room_da.find_all_room()