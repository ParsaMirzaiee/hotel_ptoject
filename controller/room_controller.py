from business_logic.room_bl import RoomBL
from model.room import Room


class RoomController:
    def __init__(self):
        self.room_bl = RoomBL()

    def save(
        self,
        room_number,
        capacity,
        bed_configuration,
        price_per_night,
        has_view,
        status
    ):
        try:
            room = Room(
                room_number,
                capacity,
                bed_configuration,
                price_per_night,
                has_view,
                status
            )

            self.room_bl.save(room)
            return "Room saved successfully."



        except Exception as error:

            return f"Operation failed: {error}"

    def find_all_room(self):
        return self.room_bl.find_all_room()