class PaymentDA:
    def __init__(self):
        self.payment_list = []

    def save(self, payment):
        self.payment_list.append(payment)

    def find_by_payment_id(self, payment_id):
        for payment in self.payment_list:
            if payment.payment_id == payment_id:
                return payment

        return None

    def find_by_reservation_id(self, reservation_id):
        result = []

        for payment in self.payment_list:
            if payment.reservation.reservation_id == reservation_id:
                result.append(payment)

        return result

    def find_all_payment(self):
        return self.payment_list