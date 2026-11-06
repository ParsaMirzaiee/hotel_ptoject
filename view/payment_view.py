import tkinter as tk
from datetime import date
from tkinter import ttk, messagebox


class PaymentView:
    def __init__(self, root, payment_controller, reservation):
        self.payment_controller = payment_controller
        self.reservation = reservation

        self.window = tk.Toplevel(root)
        self.window.title("Payment")
        self.window.geometry("350x300")

        total_amount = self.reservation.calculate_total()

        ttk.Label(
            self.window,
            text=f"Reservation ID: {self.reservation.reservation_id}"
        ).pack(anchor="w", padx=15, pady=(15, 8))

        ttk.Label(
            self.window,
            text=f"Amount: {total_amount}"
        ).pack(anchor="w", padx=15, pady=8)

        ttk.Label(self.window, text="Payment method:").pack(
            anchor="w",
            padx=15
        )

        self.payment_method_combo = ttk.Combobox(
            self.window,
            values=["cash", "card"],
            state="readonly"
        )
        self.payment_method_combo.current(0)
        self.payment_method_combo.pack(fill="x", padx=15, pady=(0, 8))

        ttk.Label(self.window, text="Transaction code:").pack(
            anchor="w",
            padx=15
        )

        self.transaction_code_entry = ttk.Entry(self.window)
        self.transaction_code_entry.pack(
            fill="x",
            padx=15,
            pady=(0, 8)
        )

        ttk.Button(
            self.window,
            text="Pay",
            command=self.save_payment
        ).pack(pady=12)

    def save_payment(self):
        payments = self.payment_controller.find_all_payment()
        payment_id = len(payments) + 1

        payment_method = self.payment_method_combo.get()
        transaction_code = self.transaction_code_entry.get()

        if payment_method == "cash":
            transaction_code = None

        result = self.payment_controller.save(
            payment_id=payment_id,
            reservation=self.reservation,
            amount=self.reservation.calculate_total(),
            payment_date=date.today(),
            payment_method=payment_method,
            payment_status="paid",
            transaction_code=transaction_code
        )

        if result == "Payment saved successfully.":
            messagebox.showinfo("Payment", result)
        else:
            messagebox.showerror("Payment", result)
