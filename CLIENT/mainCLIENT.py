import requests
import os
import shutil
import json
from Models import *

def getElementBy(keyDict, targetValue, thisDict):
    for key, value in thisDict.items():
        if value[f"{keyDict}"] == targetValue:
            return thisDict[key]
    return {}

def getElementsBy(keyDict, targetValue, thisDict):
    eleDict = {}
    for key, value in thisDict.items():
        if value[f"{keyDict}"] == targetValue:
            # return thisDict[key]
            eleDict[key] = value
    return eleDict

class CLIENT:
    def __init__(self, username) -> None:
        self.BASE = "http://127.0.0.1:5000/"
        try:
            data = requests.get(self.BASE).json()
        except:
            data = {"status":"ERROR"}
        with open("api.json", "w", encoding='utf-8') as outfile:
            json.dump(data, outfile,ensure_ascii=False)
        f = open('api.json', 'r',encoding='utf-8')
        self.dataJson = json.load(f)
        print(getElementBy('id',username, self.dataJson['users']))
        self.user = User.fromJson(getElementBy('id',username, self.dataJson['users']))
        f.close()

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
    
    def getLibrary(self):
        transaction_id = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('user_id', self.user.id, self.dataJson['transactions'])]
        # print(transaction_id)

        return [self.dataJson['games'][item] for item in self.dataJson['games'] if self.dataJson['games'][item]['id'] in transaction_id]
    
    def getLibraryByStr(self, strSearch):
        transaction_id = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('user_id', self.user.id, self.dataJson['transactions'])]
        return [self.dataJson['games'][item] for item in self.dataJson['games'] if (self.dataJson['games'][item]['id'] in transaction_id and (str(self.dataJson['games'][item]['id']) == strSearch or self.dataJson['games'][item]['name'] == strSearch))]
    
    def getGameByStr(self, strSearch):
        return requests.get(self.BASE + f'games/where/{strSearch}').json()

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
    
    def get_user_image_path(self, filename):
        img_data = requests.get(self.BASE + f'/images/users/{filename}').content
        if not os.path.exists(f'Assets/images/users/{filename}'):
            open(filename, 'w').close()
        if not os.path.exists(f'Assets/images/users/{filename}'):
            os.rename(filename, f'Assets/images/users/{filename}')
        with open(f'Assets/images/users/{filename}', 'wb') as handler:
            handler.write(img_data)
        return f'Assets/images/users/{filename}'


