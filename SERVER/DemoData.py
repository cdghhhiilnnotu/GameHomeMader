import psycopg2
import json
from helper import tuple2dict, listDict, getListData

conn = psycopg2.connect(host="localhost", dbname="GamesTrader", user="postgres",
                        password="1009", port=5432)
conn.set_client_encoding('UTF8')

cur = conn.cursor()

users, usersColumn = getListData(cur, "users")
listUsers = listDict(users, usersColumn)
conn.commit()

games, gamesColumn = getListData(cur, "games")
listGames = listDict(games, gamesColumn)

cur.execute("""
    select price, user_id, game_id, id, to_char(created_at, 'yyyy-MM-dd'), to_char(updated_at, 'yyyy-MM-dd'), status from transactions
""")
transactions = cur.fetchall()

cur.execute(f"""
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = 'transactions';
""")
transactionsColumn = [x[0] for x in cur.fetchall()]

listTransactions = listDict(transactions, transactionsColumn)

payments, paymentsColumn = getListData(cur, "payments")
listPayments = listDict(payments, paymentsColumn)

dictGames = {}
for i in range(len(listGames)):
    dictGames[f'game{i}'] = listGames[i]

dictUsers = {}
for i in range(len(listUsers)):
    dictUsers[f'user{i}'] = listUsers[i]
# print(dictUsers['user1'])

dictTransactions = {}
for i in range(len(listTransactions)):
    dictTransactions[f'transaction{i}'] = listTransactions[i]

dictPayments = {}
for i in range(len(listPayments)):
    dictPayments[f'payment{i}'] = listPayments[i]

jsonDict = {}

jsonDict['users'] = dictUsers
jsonDict['games'] = dictGames
jsonDict['transactions'] = dictTransactions
jsonDict['payments'] = dictPayments

# json_object = json.dumps(jsonDict)

# with open("sample1.json", "w", encoding='utf-8') as outfile:
#     json.dump(jsonDict, outfile,ensure_ascii=False)

conn.commit()
cur.close()
conn.close()


