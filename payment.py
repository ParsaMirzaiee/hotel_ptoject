class Payment:
    def __init__(self,payment_id,amount,payment_date,payment_method,status,transaction_code):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_date = payment_date
        self.payment_method = payment_method
        self.status = status
        self.transaction_code = transaction_code


    def proccess_payment(self):
        pass
