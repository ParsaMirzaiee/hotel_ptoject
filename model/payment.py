class Payment:
    def __init__(self,payment_id,amount,payment_date,payment_method,status,transaction_code):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.status = status
        self.transaction_code = transaction_code


    @property
    def payment_id(self):
        return self.__payment_id
    @payment_id.setter
    def payment_id(self,payment_id):
        payment_id_validation(payment_id)
        self.__payment_id = payment_id


    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,amount):
        amount_validation(amount)
        self.__amount = amount


    @property
    def payment_date(self):
        return self.__payment_date
    @payment_date.setter
    def payment_date(self,payment_date):
        payment_date_validation(payment_date)
        self.__payment_date = payment_date


    @property
    def payment_method(self):
        return self.__payment_method
    @payment_method.setter
    def payment_method(self,payment_method):
        payment_method_validation(payment_method)
        self.__payment_method = payment_method


    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self,status):
        status_validation(status)
        self.__status = status


    @property
    def transaction_code(self):
        return self.__transaction_code
    @transaction_code.setter
    def transaction_code(self,transaction_code):
        transaction_code_validation
        self.__transaction_code = transaction_code



