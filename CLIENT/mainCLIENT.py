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

def searchInJsonElements(search, jsonBlock):
    for key in jsonBlock:
        if search in str(jsonBlock[key]).split(" "):
            return True
    return False

class CLIENT:
    def __init__(self, user_email='') -> None:
        self.BASE = "http://127.0.0.1:5000/"
        self.reset_api()
        self.user = self.get_user(user_email)

    def get_api_json(self):
        try:
            data = requests.get(self.BASE).json()
            with open("api.json", "w", encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
        except:
            print("FAIL TO GET API")

    def read_api(self):
        data = {}
        with open('api.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def reset_api(self):
        self.get_api_json()
        self.dataJson = self.read_api()
        self.init_game_images()

    def get_user(self, user_email):
        return getElementBy('email', user_email, self.dataJson['users'])
    
    def putUser(self, id, updated_user):
        return requests.put(self.BASE + f'users/{id}', data=updated_user)
    
    def init_game_images(self):
        for game in self.dataJson['games']:
            filename = f'game{game["id"]}.png'
            if not os.path.exists(f'Assets/images/games/{filename}'):
                img_data = requests.get(game['images']).content
                if not os.path.exists(f'Assets/images/games/{filename}'):
                    open(filename, 'w').close()
                if not os.path.exists(f'Assets/images/games/{filename}'):
                    os.rename(filename, f'Assets/images/games/{filename}')
                with open(f'Assets/images/games/{filename}', 'wb') as handler:
                    handler.write(img_data)

    def get_game_image_by_id(self, game_id):
        return f'Assets/images/games/game{game_id}.png'
    
    def get_list_games_home(self):
        list_transactions_by_user = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        list_id_games_completed = [item['game_id'] for item in list_transactions_by_user if item['status'] == 'completed']
        list_games = [game for game in self.dataJson['games'] if game['id'] not in list_id_games_completed]
        return list_games

    def get_list_games_home_by_search(self, searchStr):
        list_transactions_by_user = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        list_id_games_completed = [item['game_id'] for item in list_transactions_by_user if item['status'] == 'completed']
        list_games = [game for game in self.dataJson['games'] if (game['id'] not in list_id_games_completed) and (searchInJsonElements(searchStr, game))]
        return list_games

    def get_list_games_library(self):
        list_transactions_by_user = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        list_id_games = [item['game_id'] for item in list_transactions_by_user if item['status'] == 'completed']
        list_games = [game for game in self.dataJson['games'] if game['id'] in list_id_games]
        return list_games
    
    def get_list_games_library_by_search(self, searchStr):
        list_transactions_by_user = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        list_id_games = [item['game_id'] for item in list_transactions_by_user if item['status'] == 'completed']
        list_games = [game for game in self.dataJson['games'] if (game['id'] in list_id_games) and (searchInJsonElements(searchStr, game))]
        return list_games
    
    def get_list_games_carts(self):
        list_transactions_by_user = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        list_id_games = [item['game_id'] for item in list_transactions_by_user if item['status'] == 'pending']
        list_games = [game for game in self.dataJson['games'] if game['id'] in list_id_games]
        list_prices = [game['price'] for game in self.dataJson['games'] if game['id'] in list_id_games]
        return list_games, sum(list_prices)

    @staticmethod
    def postUser(new_user):
        return requests.post('http://127.0.0.1:5000/users', data=new_user)
    
    @staticmethod
    def getAPI():
        try:
            data = requests.get("http://127.0.0.1:5000/").json()
            with open("api.json", "w", encoding='utf-8') as outfile:
                json.dump(data, outfile, ensure_ascii=False)
        except:
            print("FAIL TO GET API")

    @staticmethod
    def readAPI():
        data = {}
        with open('api.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def post_transaction(self, new_transaction):
        list_game_carts, _ = self.get_list_games_carts()
        for game in list_game_carts:
            if game['id'] == new_transaction['game_id']:
                return {}
        return requests.post(self.BASE + 'transactions', data=new_transaction)

    def postPayment(self, new_payment):
        return requests.post(self.BASE + 'payments', data=new_payment)

    def get_pending_id(self):
        self.transactions_list = getElementsBy('user_id', self.user['id'], self.dataJson['transactions']) 
        id_pending_transac = [transac['id'] for transac in self.transactions_list if transac['status'] == 'pending']
        return id_pending_transac
    
    def get_pending_amount(self):
        self.transactions_list = getElementsBy('user_id', self.user['id'], self.dataJson['transactions']) 
        amount_pending_transac = [transac['price'] for transac in self.transactions_list if transac['status'] == 'pending']
        return amount_pending_transac

    def deleteTransactionByID(self, id_deleted):
        list_transactions = getElementsBy('user_id', self.user['id'], self.dataJson['transactions'])
        id_trans = [transac['id'] for transac in list_transactions if transac['status'] == 'pending'
                                                                                and transac['game_id'] == id_deleted]
        return requests.delete(self.BASE + f'transactions/{id_trans[0]}')
    
    @staticmethod
    def deletePayment(id):
        requests.delete("http://127.0.0.1:5000/" + f'payments/{id}')

    @staticmethod
    def deleteTransaction(id):
        requests.delete("http://127.0.0.1:5000/" + f'transactions/{id}')

    @staticmethod
    def deleteUser(id):
        requests.delete("http://127.0.0.1:5000/" + f'users/{id}')

    @staticmethod
    def postUser(new_user):
        requests.post("http://127.0.0.1:5000/" + f'users', new_user)

    @staticmethod
    def putUser(id, new_user):
        requests.put("http://127.0.0.1:5000/" + f'users/{id}', new_user)

    @staticmethod
    def deleteGame(id):
        requests.delete("http://127.0.0.1:5000/" + f'games/{id}')

    @staticmethod
    def postGame(new_game):
        requests.post("http://127.0.0.1:5000/" + f'games', new_game)

    @staticmethod
    def putGame(id, new_game):
        requests.put("http://127.0.0.1:5000/" + f'games/{id}', new_game)

# myCLIENT = CLIENT('nguyenee@example.com')
# myCLIENT.deleteTransaction(5)

