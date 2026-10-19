from business_logic.payment_bl import PaymentBL
from model.payment import Payment


class PaymentController:
    def __init__(self):
        self.payment_bl = PaymentBL()

    def save(
        self,
        payment_id,
        reservation,
        amount,
        payment_date,
        payment_method,
        payment_status,
        transaction_code=None
    ):
        try:
            payment = Payment(
                payment_id,
                reservation,
                amount,
                payment_date,
                payment_method,
                payment_status,
                transaction_code
            )

            self.payment_bl.save(payment)
            return "Payment saved successfully."

        except Exception as error:
            return f"Operation failed: {error}"

    def find_all_payment(self):
        return self.payment_bl.find_all_payment()