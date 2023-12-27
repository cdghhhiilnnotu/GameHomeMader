import requests
import os
import shutil

class CLIENT:
    def __init__(self) -> None:
        self.BASE = "http://127.0.0.1:5000/"

    def getUser(self, id=-1):
        if id==-1:
            return requests.get(self.BASE + 'users').json()
        return requests.get(self.BASE + f'users/{id}').json()

    def getTransaction(self, id=-1):
        if id==-1:
            return requests.get(self.BASE + 'transactions').json()
        return requests.get(self.BASE + f'transactions/{id}').json()

    def getPayment(self, id=-1):
        if id==-1:
            return requests.get(self.BASE + 'payments').json()
        return requests.get(self.BASE + f'payments/{id}').json()

    def getGame(self, id=-1):
        if id==-1:
            return requests.get(self.BASE + 'games').json()
        return requests.get(self.BASE + f'games/{id}').json()
    
    def getGameByStr(self, str):
        return requests.get(self.BASE + f'games/where/{str}').json()

    def postGame(self, new_game):
        return requests.post(self.BASE + 'games', data=new_game)

    def postUser(self, new_user):
        return requests.post(self.BASE + 'users', data=new_user)

    def postTransaction(self, new_transaction):
        return requests.post(self.BASE + 'transactions', data=new_transaction)

    def postUser(self, new_user):
        return requests.post(self.BASE + 'users', data=new_user)

    def putGame(self, id, updated_game):
        if id != -1:
            return requests.put(self.BASE + f'games/{id}', data=updated_game)
        return 'CANNOT DO'

    def putUser(self, id, updated_user):
        if id != -1:
            return requests.put(self.BASE + f'users/{id}', data=updated_user)
        return 'CANNOT DO'

    def putTransaction(self, id, updated_transaction):
        if id != -1:
            return requests.put(self.BASE + f'transactions/{id}', data=updated_transaction)
        return 'CANNOT DO'

    def putPayment(self, id, updated_payment):
        if id != -1:
            return requests.put(self.BASE + f'payments/{id}', data=updated_payment)
        return 'CANNOT DO'

    def deleteGame(self, id=-1):
        if id != -1:
            return requests.delete(self.BASE + f'games/{id}')
        return 'CANNOT DO'

    def deleteUser(self, id=-1):
        if id != -1:
            return requests.delete(self.BASE + f'users/{id}')
        return 'CANNOT DO'

    def deleteTransaction(self, id=-1):
        if id != -1:
            return requests.delete(self.BASE + f'transactions/{id}')
        return 'CANNOT DO'

    def deleteUser(self, id=-1):
        if id != -1:
            return requests.delete(self.BASE + f'users/{id}')
        return 'CANNOT DO'
    
    def get_game_image_path(self, filename):
        img_data = requests.get(self.BASE + f'/images/games/{filename}').content
        if not os.path.exists(f'Assets/images/games/{filename}'):
            open(filename, 'w').close()
        if not os.path.exists(f'Assets/images/games/{filename}'):
            os.rename(filename, f'Assets/images/games/{filename}')
        with open(f'Assets/images/games/{filename}', 'wb') as handler:
            handler.write(img_data)
        return f'Assets/images/games/{filename}'


