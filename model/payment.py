from tools.validation import *

class Payment:
    def __init__(
        self,
        payment_id,
        reservation,
        amount,
        payment_date,
        payment_method,
        payment_status,
        transaction_code=None
    ):
        self.payment_id = payment_id
        self.reservation = reservation
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.transaction_code = transaction_code

    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        payment_id_validator(payment_id)
        self.__payment_id = payment_id

    @property
    def reservation(self):
        return self.__reservation

    @reservation.setter
    def reservation(self, reservation):
        self.__reservation = reservation

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        amount_validator(amount)
        self.__amount = amount

    @property
    def payment_date(self):
        return self.__payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        payment_date_validator(payment_date)
        self.__payment_date = payment_date

    @property
    def payment_method(self):
        return self.__payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        payment_method_validator(payment_method)
        self.__payment_method = payment_method

    @property
    def payment_status(self):
        return self.__payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        payment_status_validator(payment_status)
        self.__payment_status = payment_status

    @property
    def transaction_code(self):
        return self.__transaction_code

    @transaction_code.setter
    def transaction_code(self, transaction_code):
        transaction_code_validator(transaction_code)
        self.__transaction_code = transaction_code



