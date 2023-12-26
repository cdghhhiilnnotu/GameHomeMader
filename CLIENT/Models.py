class User():
    usernumber = 4
    def __init__(self, id:int, name, password, email) -> None:
        User.usernumber+=1
        self.id = id
        self.name = name
        self.password = password
        self.email = email

    def toJson(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'password' : self.password,
            'email' : self.email
        }
    
    @staticmethod
    def fromJson(jsonUser):
        newUser = User(
            int(jsonUser['id']),
            jsonUser['name'],
            jsonUser['password'],
            jsonUser['email']
        )
        return newUser
    
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


class Game():
    game_number=4
    def __init__(self, demo_file, description, gender, id:int, images, name, price:float, videos) -> None:
        Game.game_number+=1
        self.demo_file = demo_file
        self.description = description
        self.gender = gender
        self.id = id
        self.images = images
        self.name = name
        self.price = price
        self.videos = videos

    def toJson(self):
        return {
            'demo_file' : self.demo_file,
            'description' : self.description,
            'gender' : self.gender,
            'id' : self.id,
            'images' : self.images,
            'name' : self.name,
            'price' : self.price,
            'videos' : self.videos
        }
    
    @staticmethod
    def fromJson(jsonGame):
        newGame = Game(
            jsonGame['demo_file'],
            jsonGame['description'],
            jsonGame['gender'],
            int(jsonGame['id']),
            jsonGame['images'],
            jsonGame['name'],
            float(jsonGame['price']),
            jsonGame['videos']
        )
        return newGame
    

class Admin():
    admin_number=0
    def __init__(self, login_name, password, name, id:int):
        Admin.admin_number+=1
        self.login_name = login_name
        self.password = password
        self.name = name
        self.id = id

    def toJson(self):
        return {
            'login_name' : self.login_name,
            'password' : self.password,
            'name' : self.name,
            'id' : self.id
        }
    
    @staticmethod
    def fromJson(jsonAdmin):
        newAdmin = Admin(
            jsonAdmin['login_name'],
            jsonAdmin['password'],
            jsonAdmin['name'],
            int(jsonAdmin['id'])
        )
        return newAdmin

