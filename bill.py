class Bill:
    def __init__(self,bill_id,issue_date,room_cost,service_cost,discount,total_amount,status):
        self.bill_id=bill_id
        self.issue_date=issue_date
        self.room_cost=room_cost
        self.service_cost=service_cost
        self.discount=discount
        self.total_amount=total_amount
        self.status=status


    def calculate_total_cost(self):
        self.total_amount = self.room_cost + self.service_cost - self.discount
        return self.total_amount
