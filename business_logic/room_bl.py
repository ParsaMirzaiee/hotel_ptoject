from data_access.room_da import RoomDA


class RoomBL:
    def __init__(self):
        self.room_da = RoomDA()

        self.room_prices = {
            (1,False):400000,
            (1,True):450000,
            (2, False): 500000,
            (2, True): 550000,
            (3, False): 600000,
            (3, True): 650000,
            (4, False): 700000,
            (4, True): 750000,
            (5, False): 800000,
            (5, True): 850000
        }

    def get_price_per_night(self,capacity,has_view):
        return self.room_prices[(capacity,has_view)]


    def save(self, room):
        existing_room = self.room_da.find_by_room_number(room.room_number)

        if existing_room is not None:
            raise ValueError("This room number already exists.")

        self.room_da.save(room)

    def find_by_room_number(self, room_number):
        return self.room_da.find_by_room_number(room_number)

    def find_all_room(self):
        return self.room_da.find_all_room()