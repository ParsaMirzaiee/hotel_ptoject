class Room:
    def __init__(self,room_number,room_type,bed_count,bed_type,capacity,price_per_night,has_view,status):

        self.room_number=room_number
        self.room_type=room_type
        self.bed_count=bed_count
        self.bed_type=bed_type
        self.capacity=capacity
        self.price_per_night=price_per_night
        self.has_view=has_view
        self.status=status


    @property
    def room_number(self):
        return self.__room_number
    @room_number.setter
    def room_number(self,room_number):
        # room_number_validation(room_number)
        self.__room_number = room_number


    @property
    def room_type(self):
        return  self.__room_type
    @room_type.setter
    def room_type(self,room_type):
        # room_type_validation(room_type)
        self.__room_type = room_type


    @property
    def bed_count(self):
        return  self.__bed_count
    @bed_count.setter
    def bed_count(self,bed_count):
        # bed_count_validation(bed_count)
        self.__bed_count = bed_count


    @property
    def bed_type(self):
        return  self.__bed_type
    @bed_type.setter
    def bed_type(self,bed_type):
        # bed_type_validation(bed_type)
        self.__bed_type = bed_type


    @property
    def capacity(self):
        return  self.__capacity
    @capacity.setter
    def capacity(self,capacity):
        # capacity_validation(capacity)
        self.__capacity = capacity

    @property
    def price_per_night(self):
        return  self.__price_per_night
    @price_per_night.setter
    def price_per_night(self,price_per_night):
        # price_per_night_validation(price_per_night)
        self.__price_per_night = price_per_night

    @property
    def has_view(self):
        return self.__has_view
    @has_view.setter
    def has_view(self,has_view):
        # has_view_validation(has_view)
        self.__has_view = has_view

    @property
    def status(self):
        return  self.__status
    @status.setter
    def status(self,status):
        # status_validator(status)
        self.__status = status



