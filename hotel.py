class Hotel:
    def __int__(self,name,address,phone_number,star_rating,check_in_time,check_out_time):

        if name or address =="":
            raise ValueError("Name or Address cannot be empty")

        if not phone_number.isdigit() or phone_number =="":
            raise ValueError("Phone number cannot be empty and should contain only digits")

        if type(star_rating)!=int or star_rating < 1 or star_rating > 5:
            raise ValueError("Star Rating should be integer between 1 and 5")


        self.name=name
        self.address=address
        self.phone_number=phone_number
        self.star_rating=star_rating
        self.check_in_time=check_in_time
        self.check_out_time=check_out_time
