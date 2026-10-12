class Room:
    def __init__(self,room_number,room_type,bed_count,bed_type,capacity,price_per_night,has_view,status):

        if not type(room_number)==int or room_number <= 0 :
            raise ValueError("Room Number must be an integer and greater than 0")

        if type(bed_count)!=int or bed_count <= 0 or type(capacity)!=int or capacity <= 0 :
            raise ValueError("Bed Count & capacity must be an integer and greater than 0")

        if price_per_night < 0:
            raise ValueError("Price per night cannot be negative")

        if type(has_view)!=bool:
            raise TypeError("has_view must be a boolean")

        if status and bed_type and room_type == "":
            raise ValueError("cannot be empty")








        self.room_number=room_number
        self.room_type=room_type
        self.bed_count=bed_count
        self.bed_type=bed_type
        self.capacity=capacity
        self.price_per_night=price_per_night
        self.has_view=has_view
        self.status=status
