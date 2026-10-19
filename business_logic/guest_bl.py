from data_access.guest_da import GuestDA


class GuestBL:
    def __init__(self):
        self.guest_da = GuestDA()

    def save(self, guest):
        existing_guest = self.guest_da.find_by_national_id(
            guest.national_id
        )

        if existing_guest is not None:
            raise ValueError("A guest with this national ID already exists.")

        self.guest_da.save(guest)

    def find_by_national_id(self, national_id):
        return self.guest_da.find_by_national_id(national_id)

    def find_all_guest(self):
        return self.guest_da.find_all_guest()