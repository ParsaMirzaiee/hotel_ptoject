class Guest:
    def __init__(self,national_id,first_name,last_name,birthdate,age,gender,phone_number):

        if not national_id.isdigit() or len(national_id) !=10:
            raise ValueError("national_id must be of length 10")

        if first_name == "":
            raise ValueError("first_name cannot be empty")
        if last_name == "":
            raise ValueError("last_name cannot be empty")

        if phone_number == "":
            raise ValueError("phone_number cannot be empty")
        if not phone_number.isdigit():
            raise ValueError("phone_number must be digits")


        self.national_id=national_id
        self.first_name=first_name
        self.last_name=last_name
        self.birthdate=birthdate
        self.age=age
        self.gender=gender
        self.phone_number=phone_number

    def __repr__(self):
        return (f"Guest(national_id={self.national_id},"
                f"first_name={self.first_name},"
                f"last_name={self.last_name},"
                f"birthdate={self.birthdate},"
                f"age={self.age},"
                f"gender={self.gender},"
                f"phone_number={self.phone_number}")



    def verify_identity(self):
        pass
