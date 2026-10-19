from data_access.payment_da import PaymentDA


class PaymentBL:
    def __init__(self):
        self.payment_da = PaymentDA()

    def save(self, payment):
        existing_payment = self.payment_da.find_by_payment_id(
            payment.payment_id
        )

        if existing_payment is not None:
            raise ValueError("This payment ID already exists.")

        reservation_payments = self.payment_da.find_by_reservation_id(
            payment.reservation.reservation_id
        )

        if reservation_payments:
            raise ValueError("This reservation already has a payment.")

        if payment.reservation.reservation_status == "cancelled":
            raise ValueError("A cancelled reservation cannot be paid.")

        if payment.amount != payment.reservation.calculate_total():
            raise ValueError("Payment amount must equal the reservation total.")

        if payment.payment_status == "paid":
            if payment.payment_date is None:
                raise ValueError("A paid payment must have a payment date.")

            if payment.payment_method == "card" and not payment.transaction_code:
                raise ValueError("A card payment must have a transaction code.")

        self.payment_da.save(payment)

    def find_all_payment(self):
        return self.payment_da.find_all_payment()

    