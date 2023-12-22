class Transaction():
    transaction_number = 4
    def __init__(self, create_at, game_id:int, id:int, price:float, status, update_at, user_id:int):
        Transaction.transaction_number+=1
        self.create_at = create_at
        self.game_id = game_id
        self.id = id
        self.price = price
        self.status = status
        self.update_at = update_at
        self.user_id = user_id

    def toJson(self):
        return {
            'create_at' : self.create_at,
            'game_id' : self.game_id,
            'id' : self.id,
            'price' : self.price,
            'status' : self.status,
            'update_at' : self.update_at,
            'user_id' : self.user_id
        }
    
    @staticmethod
    def fromJson(jsonTransaction):
        newTransaction = Transaction(
            jsonTransaction['create_at'],
            int(jsonTransaction['game_id']),
            int(jsonTransaction['id']),
            float(jsonTransaction['price']),
            jsonTransaction['status'],
            jsonTransaction['update_at'],
            int(jsonTransaction['user_id'])
        )
        return newTransaction