import psycopg2
import json
from Commons.helper import tuple2dict, listDict, getListData, getListDataWhere

class DATABASE():
    def __init__(self):
        self.jsonData = {}
        
        self.getData()

    def initConnection(self):
        self.conn = psycopg2.connect(host="localhost", dbname="GamesTrader", user="postgres",
                        password="1009", port=5432)
        self.conn.set_client_encoding('UTF8')

        self.cur = self.conn.cursor()

    def selectGameWhere(self, searchStr):
        self.initConnection()
        games, gamesColumn = getListDataWhere(self.cur, "games", searchStr)
        listGames = listDict(games, gamesColumn)
        dictGames = {}
        for i in range(len(listGames)):
            dictGames[f'game{listGames[i]["id"]-1}'] = listGames[i]
        return dictGames
    
    def selectGame(self):
        games, gamesColumn = getListData(self.cur, "games")
        listGames = listDict(games, gamesColumn)
        self.dictGames = {}
        for i in range(len(listGames)):
            self.dictGames[f'game{i}'] = listGames[i]
        return self.dictGames

    def selectUser(self):
        users, usersColumn = getListData(self.cur, "users")
        listUsers = listDict(users, usersColumn)
        self.dictUsers = {}
        for i in range(len(listUsers)):
            self.dictUsers[f'user{i}'] = listUsers[i]
        return self.dictUsers

    def selectTransaction(self):
        self.cur.execute("""
            SELECT price, 
                user_id, 
                game_id, 
                id, 
                to_char(created_at, 'yyyy-MM-dd'), 
                to_char(updated_at, 'yyyy-MM-dd'), 
                status 
            FROM transactions
        """)
        transactions = self.cur.fetchall()
        self.cur.execute(f"""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'transactions';
        """)
        transactionsColumn = [x[0] for x in self.cur.fetchall()]
        listTransactions = listDict(transactions, transactionsColumn)

        self.dictTransactions = {}
        for i in range(len(listTransactions)):
            self.dictTransactions[f'transaction{i}'] = listTransactions[i]
        return self.dictTransactions
    
    def selectPayment(self):
        payments, paymentsColumn = getListData(self.cur, "payments")
        listPayments = listDict(payments, paymentsColumn)
        self.dictPayments = {}
        for i in range(len(listPayments)):
            self.dictPayments[f'payment{i}'] = listPayments[i]
        return self.dictPayments

    def getData(self):
        self.initConnection()
        self.jsonData['users'] = self.selectUser()
        self.jsonData['games'] = self.selectGame()
        self.jsonData['transactions'] = self.selectTransaction()
        self.jsonData['payments'] = self.selectPayment()
        self.__close__()
        return self.jsonData
    
    def __close__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def insertGame(self, new_game):
        self.initConnection()
        self.cur.execute(f"""
            INSERT INTO games (name, genre, description, price, demo_file, images, videos)
            VALUES
            ({new_game['name']}, {new_game['genre']}, {new_game['description']}, {new_game['price']}, {new_game['demo_file']}, {new_game['images']}, {new_game['videos']})
        """)
        self.__close__()

    def insertUser(self, new_user):
        self.initConnection()
        self.cur.execute(f"""
            INSERT INTO users (name, email, password)
            VALUES
            ({new_user['name']}, {new_user['email']}, {new_user['password']})
        """)
        self.__close__()

    def insertTransaction(self, new_transaction):
        self.initConnection()
        self.cur.execute(f"""
            INSERT INTO transactions (user_id, game_id, price, status, created_at, updated_at)
            VALUES
            ({new_transaction['user_id']}, {new_transaction['game_id']}, {new_transaction['price']}, {new_transaction['status']}, {new_transaction['created_at']}, {new_transaction['updated_at']})
        """)
        self.__close__()

    def insertPayment(self, new_payment):
        self.initConnection()
        self.cur.execute(f"""
            INSERT INTO payments (transaction_id, payment_method, amount, transaction_id_number)
            VALUES
            ({new_payment['transaction_id']}, '{new_payment['payment_method']}', {new_payment['amount']}, '{new_payment['transaction_id_number']}')
        """)
        self.__close__()

# jsonDict = returnData(cur)

# json_object = json.dumps(jsonDict)

# with open("sample1.json", "w", encoding='utf-8') as outfile:
#     json.dump(jsonDict, outfile,ensure_ascii=False)




