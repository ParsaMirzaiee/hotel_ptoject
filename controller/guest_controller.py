from business_logic.guest_bl import GuestBL
from model.customers import Guest


class GuestController:
    def __init__(self):
        self.guest_bl = GuestBL()

    def save(
        self,
        national_id,
        first_name,
        last_name,
        birthdate,
        gender,
        phone_number
    ):
        try:
            guest = Guest(
                national_id,
                first_name,
                last_name,
                birthdate,
                gender,
                phone_number
            )

            self.guest_bl.save(guest)
            return "Guest saved successfully."


        except Exception as error:

            return f"Operation failed: {error}"



    def find_by_national_id(self, national_id):
        return self.guest_bl.find_by_national_id(national_id)

    def find_all_guest(self):
        return self.guest_bl.find_all_guest()