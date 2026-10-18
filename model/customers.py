from tools.validation import *
from datetime import datetime


class Guest:
    def __init__(self, national_id, first_name, last_name, birthdate, age, gender, phone_number):
        self.national_id = national_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    @property
    def national_id(self):
        return self.__national_id

    @national_id.setter
    def national_id(self, national_id):
        national_id_validator(national_id)
        self.__national_id = national_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        first_name_validator(first_name)
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        last_name_validator(last_name)
        self.__last_name = last_name

    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        birthdate_validator(birthdate)
        self.__birthdate = birthdate


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        gender_validator(gender)
        self.__gender = gender

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        phone_number_validator(phone_number)
        self.__phone_number = phone_number
