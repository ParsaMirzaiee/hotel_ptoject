from tools.validation import *


class Room:
    def __init__(self,room_number,capacity,bed_configuration,price_per_night,has_view,status):

        self.room_number=room_number
        self.capacity=capacity
        self.bed_configuration=bed_configuration
        self.price_per_night=price_per_night
        self.has_view=has_view
        self.status=status


    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self,room_number):
        room_number_validator(room_number)
        self.__room_number = room_number



    @property
    def capacity(self):
        return  self.__capacity

    @capacity.setter
    def capacity(self,capacity):
        capacity_validator(capacity)
        self.__capacity = capacity


    @property
    def bed_configuration(self):
        return self.__bed_configuration

    @bed_configuration.setter
    def bed_configuration(self, bed_configuration):
        bed_configuration_validator(self.capacity,bed_configuration)
        self.__bed_configuration = bed_configuration


    @property
    def price_per_night(self):
        return  self.__price_per_night

    @price_per_night.setter
    def price_per_night(self,price_per_night):
        price_per_night_validator(price_per_night)
        self.__price_per_night = price_per_night

    @property
    def has_view(self):
        return self.__has_view

    @has_view.setter
    def has_view(self,has_view):
        has_view_validator(has_view)
        self.__has_view = has_view

    @property
    def status(self):
        return  self.__status

    @status.setter
    def status(self,status):
        status_validator(status)
        self.__status = status



    
