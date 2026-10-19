class GuestDA:
    def __init__(self):
        self.guest_list = []

    def save(self, guest):
        self.guest_list.append(guest)

    def find_by_national_id(self, national_id):
        for guest in self.guest_list:
            if guest.national_id == national_id:
                return guest

        return None

    def find_all_guest(self):
        return self.guest_list