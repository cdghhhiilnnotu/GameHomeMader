import requests
import os
import shutil
import json
from Models import *

def getElementBy(keyDict, targetValue, thisDict):
    for item in thisDict:
        if item[f"{keyDict}"] == targetValue:
            return item
    return {}

def getElementsBy(keyDict, targetValue, thisDict):
    eleDict = []
    for item in thisDict:
        if item[f"{keyDict}"] == targetValue:
            eleDict.append(item)
    return eleDict

class CLIENT:
    def __init__(self, user_email) -> None:
        self.BASE = "http://127.0.0.1:5000/"
        self.get_api_json()
        
        self.user_id = self.get_user_id(user_email)
        self.user_password = self.get_user(user_email)['password']

        self.user = getElementBy('id', self.user_id, self.dataJson['users'])
        self.transactions_list = getElementsBy('user_id', self.user_id, self.dataJson['transactions'])  
        # print(self.get_cart_games())

    def resetApi(self):
        self.get_api_json()
        self.transactions_list = getElementsBy('user_id', self.user_id, self.dataJson['transactions'])  

    def get_api_json(self):
        try:
            data = requests.get(self.BASE).json()
        except:
            data = {"status":"ERROR"}
        with open("api.json", "w", encoding='utf-8') as outfile:
            json.dump(data, outfile, ensure_ascii=False)
        f = open('api.json', 'r', encoding='utf-8')
        self.dataJson = json.load(f)
        f.close()

    def get_home_games(self):
        id_completed_games = [id_game['game_id'] for id_game in self.transactions_list if id_game['status'] == 'completed']
        games = [game for game in self.dataJson['games'] if game['id'] not in id_completed_games]
        return games
    
    def get_home_games_by_search(self, searchStr):
        id_completed_games = [id_game['game_id'] for id_game in self.transactions_list if id_game['status'] == 'completed']
        games = [game for game in self.dataJson['games'] if game['id'] not in id_completed_games 
                                                            and (str(game['id']) in searchStr
                                                                 or 
                                                                 str(game['name']) in searchStr)]
        return games
        
    def get_library_games(self):
        id_completed_games = [id_game['game_id'] for id_game in self.transactions_list if id_game['status'] == 'completed']
        games = [game for game in self.dataJson['games'] if game['id'] in id_completed_games]
        return games
    
    def get_library_games_by_search(self, searchStr):
        id_completed_games = [id_game['game_id'] for id_game in self.transactions_list if id_game['status'] == 'completed']
        games = [game for game in self.dataJson['games'] if game['id'] in id_completed_games 
                                                            and (str(game['id']) in searchStr
                                                                 or 
                                                                 str(game['name']) in searchStr)]
        return games

    def get_cart_games(self):
        self.get_api_json()
        self.transactions_list = getElementsBy('user_id', self.user_id, self.dataJson['transactions'])  
        id_pending_games = [id_game['game_id'] for id_game in self.transactions_list if id_game['status'] == 'pending']
        games = [game for game in self.dataJson['games'] if game['id'] in id_pending_games]
        totalCost = [game['price'] for game in self.dataJson['games'] if game['id'] in id_pending_games]
        self.totalCost = sum(totalCost)
        # print(id_pending_games)
        return games

    def get_user_id(self, user_email):
        return getElementBy('email', user_email, self.dataJson['users'])['id']

    def get_user(self, user_email):
        return getElementBy('email', user_email, self.dataJson['users'])

    @staticmethod
    def postUser(new_user):
        return requests.post('http://127.0.0.1:5000/users', data=new_user)


    # def getUser(self, id=-1):
    #     if id==-1:
    #         return requests.get(self.BASE + 'users').json()
    #     return requests.get(self.BASE + f'users/{id}').json()

    # def getTransaction(self, id=-1):
    #     transaction_id_user = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('user_id', self.user.id, self.dataJson['transactions'])]
    #     transaction_id_status = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('status', 'completed', self.dataJson['transactions'])]
    #     # print(transaction_id_user)

    #     return [self.dataJson['games'][item] for item in self.dataJson['games'] if self.dataJson['games'][item]['id'] in transaction_id_user and self.dataJson['games'][item]['id'] in transaction_id_status]
    #     # if id==-1:
    #     #     return requests.get(self.BASE + 'transactions').json()
    #     # return requests.get(self.BASE + f'transactions/{id}').json()

    # def getPayment(self, id=-1):
    #     if id==-1:
    #         return requests.get(self.BASE + 'payments').json()
    #     return requests.get(self.BASE + f'payments/{id}').json()

    # def getGame(self, id=-1):
    #     if id==-1:
    #         return requests.get(self.BASE + 'games').json()
    #     return requests.get(self.BASE + f'games/{id}').json()
    
    # def getLibrary(self):
    #     transaction_id = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('user_id', self.user.id, self.dataJson['transactions'])]
    #     # print(transaction_id)

    #     return [self.dataJson['games'][item] for item in self.dataJson['games'] if self.dataJson['games'][item]['id'] in transaction_id]
    
    # def getLibraryByStr(self, strSearch):
    #     transaction_id = [self.dataJson['transactions'][item]['game_id'] for item in getElementsBy('user_id', self.user.id, self.dataJson['transactions'])]
    #     return [self.dataJson['games'][item] for item in self.dataJson['games'] if (self.dataJson['games'][item]['id'] in transaction_id and (str(self.dataJson['games'][item]['id']) == strSearch or self.dataJson['games'][item]['name'] == strSearch))]
    
    # def getGameByStr(self, strSearch):
    #     return requests.get(self.BASE + f'games/where/{strSearch}').json()

    # def postGame(self, new_game):
    #     return requests.post(self.BASE + 'games', data=new_game)

    # def postUser(self, new_user):
    #     return requests.post(self.BASE + 'users', data=new_user)

    # def postTransaction(self, new_transaction):
    #     return requests.post(self.BASE + 'transactions', data=new_transaction)

    def postPayment(self, new_payment):
        return requests.post(self.BASE + 'payments', data=new_payment)

    # def putGame(self, id, updated_game):
    #     if id != -1:
    #         return requests.put(self.BASE + f'games/{id}', data=updated_game)
    #     return 'CANNOT DO'

    def get_pending_id(self):
        self.get_api_json()
        self.transactions_list = getElementsBy('user_id', self.user_id, self.dataJson['transactions']) 
        id_pending_transac = [transac['id'] for transac in self.transactions_list if transac['status'] == 'pending']
        return id_pending_transac
    
    def get_pending_amount(self):
        self.get_api_json()
        self.transactions_list = getElementsBy('user_id', self.user_id, self.dataJson['transactions']) 
        amount_pending_transac = [transac['price'] for transac in self.transactions_list if transac['status'] == 'pending']
        return amount_pending_transac

    def putUser(self, id, updated_user):
        self.get_api_json()
        return requests.put(self.BASE + f'users/{id}', data=updated_user)

    def putTransaction(self, id, updated_transaction):
        return requests.put(self.BASE + f'transactions/{id}', data=updated_transaction)
    
    def post_transaction(self, new_transaction):
        return requests.post(self.BASE + 'transactions', data=new_transaction)

    # def putPayment(self, id, updated_payment):
    #     if id != -1:
    #         return requests.put(self.BASE + f'payments/{id}', data=updated_payment)
    #     return 'CANNOT DO'

    # def deleteGame(self, id=-1):
    #     if id != -1:
    #         return requests.delete(self.BASE + f'games/{id}')
    #     return 'CANNOT DO'

    # def deleteUser(self, id=-1):
    #     if id != -1:
    #         return requests.delete(self.BASE + f'users/{id}')
    #     return 'CANNOT DO'

    def deleteTransaction(self, id_deleted):
        id_trans = [transac['id'] for transac in self.transactions_list if transac['status'] == 'pending'
                                                                                and transac['game_id'] == id_deleted]
        # print(id_trans)
        # id_deleted = getElementBy('game_id', id, self.dataJson['transactions'])['id']
        return requests.delete(self.BASE + f'transactions/{id_trans[0]}')

    # def deleteUser(self, id=-1):
    #     if id != -1:
    #         return requests.delete(self.BASE + f'users/{id}')
    #     return 'CANNOT DO'
    
    def get_game_image_path(self, urlImg, game_name):
        print(game_name)
        filename = game_name + '.png'
        img_data = requests.get(urlImg).content
        if not os.path.exists(f'Assets/images/games/{filename}'):
            print('open')
            open(filename, 'w').close()
        if os.path.exists(filename):
            print('created ' + filename)
        if not os.path.exists(f'Assets/images/games/{filename}'):
            print('rename ' + filename)
            os.rename(filename, f'Assets/images/games/{filename}')
        with open(f'Assets/images/games/{filename}', 'wb') as handler:
            print('write')
            handler.write(img_data)
        print(f'Assets/images/games/{filename}')
        return f'Assets/images/games/{filename}'
    
    # def get_user_image_path(self, filename):
    #     img_data = requests.get(self.BASE + f'/images/users/{filename}').content
    #     if not os.path.exists(f'Assets/images/users/{filename}'):
    #         open(filename, 'w').close()
    #     if not os.path.exists(f'Assets/images/users/{filename}'):
    #         os.rename(filename, f'Assets/images/users/{filename}')
    #     with open(f'Assets/images/users/{filename}', 'wb') as handler:
    #         handler.write(img_data)
    #     return f'Assets/images/users/{filename}'


