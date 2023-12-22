class Payment():
    payment_number = 3
    def __init__(self, amount:float, id:int, payment_method, transaction_id:int, transaction_id_number):
        Payment.payment_number+=1
        self.amount = amount
        self.id = id
        self.payment_method = payment_method
        self.transaction_id = transaction_id
        self.transaction_id_number = transaction_id_number

    def toJson(self):
        return {
            'amount' : self.amount,
            'id' : self.id,
            'payment_method' : self.payment_method,
            'transaction_id' : self.transaction_id,
            'transaction_id_number' : self.transaction_id_number
        }
    
    @staticmethod
    def fromJson(jsonPayment):
        newPayment = Payment(
            float(jsonPayment['amount']),
            int(jsonPayment['id']),
            jsonPayment['payment_method'],
            int(jsonPayment['transaction_id']),
            jsonPayment['transaction_id_number']
        )
        return newPayment

