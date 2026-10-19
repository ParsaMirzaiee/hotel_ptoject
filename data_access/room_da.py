class RoomDA:
    def __init__(self):
        self.room_list = []

    def save(self, room):
        self.room_list.append(room)

    def find_by_room_number(self, room_number):
        for room in self.room_list:
            if room.room_number == room_number:
                return room

        return None

    def find_all_room(self):
        return self.room_list

