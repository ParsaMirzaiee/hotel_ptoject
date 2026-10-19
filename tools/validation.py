import re
from datetime import date

#=========================================================================================================================
#customer_validation
#=========================================================================================================================
def national_id_validator(national_id):
    if not isinstance(national_id, str) or not re.match(r"^(\d{10}|\d{3}-\d{6}-\d)$", national_id):
        raise ValueError("invalid national id !!!")
    return national_id


def first_name_validator(first_name):
    if not isinstance(first_name, str) or not re.match(r"^[a-zA-Z\s]{3,50}$", first_name):
        raise ValueError("invalid first name !!!")
    return first_name


def last_name_validator(last_name):
    if not isinstance(last_name, str) or not re.match(r"^[a-zA-Z\s]{3,50}$", last_name):
        raise ValueError("invalid last name !!!")
    return last_name


def birthdate_validator(birthdate):
    if not isinstance(birthdate,date):
        raise ValueError("Birthdate must be entered az date| format:yyyy-mm-dd")

    if birthdate > date.today():
        raise ValueError("Birthdate cannot be in the future")


def gender_validator(gender):
    if not isinstance(gender, str) or not re.match ("male|female", gender):
        raise ValueError("invalid gender !!!")
    return gender



def phone_number_validator(phone_number):
    if not isinstance(phone_number, str) or not re.match(r"^(09\d{9}|\+989\d{9})$", phone_number):
        raise ValueError("invalid phone number !!!")
    return phone_number

#=========================================================================================================================
#room_validation
#=========================================================================================================================
def room_number_validator(room_number):
    if not isinstance(room_number, int) or not (0 < int(room_number) <=500):
        raise ValueError("invalid room number !!!")
    return room_number


def capacity_validator(capacity):
    if not isinstance(capacity, int) or not (1 <= int(capacity) <=5):
              raise ValueError("invalid capacity !!!")
    return capacity


def bed_configuration_validator(capacity,bed_configuration):
    allowed_configuration = {1:"1 single bed",2:"1 double bed",3:"1 double bed + 1 single bed",4:"2 double beds",5:"2 double beds + 1 single bed"}

    if capacity not in allowed_configuration:
        raise ValueError("capacity must be between 1 and 5 !!!")

    if bed_configuration != allowed_configuration[capacity]:
        raise ValueError("bed_configuration does not match room capacity !!!")


def price_per_night_validator(price_per_night):
    if not isinstance(price_per_night, int) or price_per_night <= 0:
        raise ValueError("price should be a number and greater than 0 !!!")
    return price_per_night


def has_view_validator(has_view):
    if not isinstance(has_view, bool):
        raise ValueError("has_view must be True or False !!!")
    return has_view


def status_validator(status):
    allowed_statuses = ("available", "unavailable", "maintenance")

    if not isinstance(status, str) or status not in allowed_statuses:
        raise ValueError("status must be one of: available, unavailable, maintenance")

#=========================================================================================================================
#reservation_validation
#=========================================================================================================================

def reservation_id_validator(reservation_id):
    if not isinstance(reservation_id, int) or reservation_id <= 0:
        raise ValueError("reservation_id should be an integer and greater than 0 !!!")
    return reservation_id


def booking_date_validator(booking_date):
    if not isinstance(booking_date, date) or booking_date > date.today():
        raise ValueError("booking_date cannot be in the future")
    return booking_date

def check_in_date_validator(check_in_date):
    if not isinstance(check_in_date, date) or check_in_date < date.today():
        raise ValueError("check_in_date cannot be in the past")
    return check_in_date


def check_out_date_validator(check_out_date):
    if not isinstance(check_out_date, date):
        raise ValueError("check_out_date must be a date")
    return check_out_date


def guest_count_validator(guest_count):
    if not isinstance(guest_count, int) or guest_count <= 0:
        raise ValueError("guest_count should be an integer and greater than 0 !!!")
    return guest_count


def reservation_status_validator(reservation_status):
    allowed_statuses = ("confirmed","cancelled")
    if not isinstance(reservation_status, str) or reservation_status not in allowed_statuses:
        raise ValueError("reservation_status must be confirmed, or cancelled")
    return reservation_status

#=========================================================================================================================
#payment_validation
#=========================================================================================================================


def payment_id_validator(payment_id):
    if not isinstance(payment_id, int) or payment_id <= 0:
        raise ValueError("payment_id should be an integer and greater than 0 !!!")
    return payment_id


def amount_validator(amount):
    if not isinstance(amount, float) or amount <= 0:
        raise ValueError("invalid amount !!!")
    return amount


def payment_date_validator(payment_date):
    if payment_date is None:
        return payment_date

    if not isinstance(payment_date,date) or payment_date > date.today():
        raise ValueError("payment_date cannot be in the future and should be a type of date |format:yyyy-mm-dd")
    return payment_date


def payment_method_validator(payment_method):
    allowed_methods = ("cash","card")
    if not isinstance(payment_method, str) or payment_method not in allowed_methods:
        raise ValueError("payment_method must be one of: cash, card")
    return payment_method



def payment_status_validator(payment_status):
    allowed_statuses = ("paid","unpaid")
    if not isinstance(payment_status, str) or payment_status not in allowed_statuses:
        raise ValueError("payment_status must be one of: paid, unpaid")
    return payment_status



def transaction_code_validator(transaction_code):
    if transaction_code is not None and not isinstance(transaction_code, str):
        raise ValueError("Transaction code must be text or None.")

    return transaction_code