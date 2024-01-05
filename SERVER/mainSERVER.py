from flask import Flask, request, jsonify, send_file, send_from_directory
from datetime import datetime
from Data.mainDB1 import *
import os
import json
import shutil

app = Flask(__name__)

# ALL ROUTE
@app.route('/', methods=['GET'])
def get_all():
    return jsonDict

# GAMES ROUTE
@app.route('/games', methods=['GET'])
def get_all_games():
    return jsonify(jsonDict['games'])

@app.route('/games/where/<searchStr>', methods=['GET'])
def get_all_games_where(searchStr):
    return jsonify(database.selectGameWhere(searchStr))

@app.route('/games/<int:game_id_get>', methods=['GET'])
def get_game_by_id(game_id_get):
    return jsonify(jsonDict['games'][f'game{game_id_get-1}'])

@app.route('/games', methods=['POST'])
def post_game():
    if int(request.form['id']) not in list(map(lambda data: data["id"], jsonDict['games'].values())):
        data = {}
        data['demo_file'] = request.form['demo_file']
        data['description'] = request.form['description']
        data['genre'] = request.form['genre']
        data['id'] = int(request.form['id'])
        data['images'] = request.form['images']
        data['name'] = request.form['name']
        data['price'] = float(request.form['price'])
        data['videos'] = request.form['videos']
        jsonDict['games'][f'game{len(jsonDict["games"])}'] = data

    return jsonify(jsonDict), 201

@app.route('/games/<int:game_id_put>', methods=['PUT'])
def put_game_by_id(game_id_put):
    for item in jsonDict['games']:
        if int(jsonDict['games'][item]['id']) == int(game_id_put):
            data = {}
            data['demo_file'] = request.form['demo_file']
            data['description'] = request.form['description']
            data['genre'] = request.form['genre']
            data['id'] = int(game_id_put)
            data['images'] = request.form['images']
            data['name'] = request.form['name']
            data['price'] = int(request.form['price'])
            data['videos'] = request.form['videos']
            jsonDict['games'][item] = data
    return jsonify(jsonDict)

@app.route('/games/<int:game_id_delete>', methods=['DELETE'])
def delete_game_by_id(game_id_delete):
    itemDelete = ''
    for item in jsonDict['games']:
        if int(jsonDict['games'][item]['id']) == int(game_id_delete):
            itemDelete = item
    jsonDict['games'].pop(itemDelete)
    return jsonify(jsonDict)


# USERS ROUTE
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(jsonDict['users'])

@app.route('/users/<int:user_id_get>', methods=['GET'])
def get_user_id(user_id_get):
    return jsonify(jsonDict['users'][f'user{user_id_get}'])

@app.route('/users', methods=['POST'])
def post_user():
    database.execute_SQL(f"""INSERT INTO users (name, email, password)
                                VALUES
                                ('{request.form["name"]}', '{request.form["email"]}', '{request.form["password"]}');""")
    database.init_data()

    return jsonify(jsonDict), 201

@app.route('/users/<int:user_id_put>', methods=['PUT'])
def put_user_by_id(user_id_put):
    database.execute_SQL(f"""UPDATE users SET email='{request.form["email"]}', name='{request.form["name"]}', password='{request.form["password"]}' WHERE id = {user_id_put};""")
    database.init_data()
    
    return jsonify(jsonDict)

@app.route('/users/<int:user_id_delete>', methods=['DELETE'])
def delete_user_by_id(user_id_delete):
    itemDelete = ''
    for item in jsonDict['users']:
        if int(jsonDict['users'][item]['id']) == int(user_id_delete):
            itemDelete = item
    jsonDict['users'].pop(itemDelete)
    return jsonify(jsonDict)


# TRANSACTIONS ROUTE
@app.route('/transactions', methods=['GET'])
def get_all_transactions():
    return jsonify(jsonDict['transactions'])

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_id(transaction_id):
    return jsonDict['transactions'][f'transaction{transaction_id-1}']

@app.route('/transactions/user/<int:user_id_get>', methods=['GET'])
def get_transaction_user_id(user_id_get):
    list_game_id = [trans['game_id'] for trans in jsonDict['transactions'] if trans['user_id'] == user_id_get and trans['status'] == 'completed']
    return jsonify([game for game in jsonDict['games'] if game['id'] in list_game_id])

@app.route('/transactions', methods=['POST'])
def post_transaction():
    database.execute_SQL(f"""INSERT INTO transactions (user_id, game_id, price, status, created_at, updated_at)
                                VALUES
                                ({request.form['user_id']}, {request.form['game_id']}, {request.form['price']}, '{request.form['status']}', '{request.form['created_at']}', '{request.form['updated_at']}');""")
    database.init_data()
    return jsonify(jsonDict), 201

@app.route('/transactions/<int:transaction_id_put>', methods=['PUT'])
def put_transaction_by_id(transaction_id_put):
    for item in jsonDict['transactions']:
        if int(jsonDict['transactions'][item]['id']) == int(transaction_id_put):
            data = {}
            data['created_at'] = request.form['created_at']
            data['game_id'] = int(request.form['game_id'])
            data['id'] = int(transaction_id_put)
            data['price'] = float(request.form['price'])
            data['status'] = request.form['status']
            data['updated_at'] = request.form['updated_at']
            data['user_id'] = int(request.form['user_id'])

            jsonDict['transactions'][item] = data
    return jsonify(jsonDict)

@app.route('/transactions/<int:transaction_id_delete>', methods=['DELETE'])
def delete_transaction_by_id(transaction_id_delete):
    database.execute_SQL(f"""DELETE FROM transactions WHERE id = {transaction_id_delete}""")
    database.init_data()

    return jsonify(jsonDict)

# PAYMENTS ROUTE
@app.route('/payments', methods=['GET'])
def get_all_payments():
    return jsonify(jsonDict['payments'])

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_id(payment_id):
    return jsonDict['payments'][f'payment{payment_id-1}']

@app.route('/payments', methods=['POST'])
def post_payment():
    database.execute_SQL(f"""INSERT INTO payments (transaction_id, payment_method, amount, transaction_id_number)
                                VALUES
                                ({request.form['transaction_id']}, '{str(request.form['payment_method'])}', {float(request.form['amount'])}, '{request.form['transaction_id_number']}')""")
    database.execute_SQL(f"""UPDATE transactions SET status='completed', updated_at='{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' WHERE id = {request.form['transaction_id']};""")
    
    database.init_data()
    
    return jsonify(jsonDict), 201

@app.route('/payments/<int:payment_id_put>', methods=['PUT'])
def put_payment_by_id(payment_id_put):
    for item in jsonDict['payments']:
        if int(jsonDict['payments'][item]['id']) == int(payment_id_put):
            data = {}
            data['amount'] = float(request.form['amount'])
            data['id'] = int(request.form['id'])
            data['payment_method'] = request.form['payment_method']
            data['transaction_id'] = float(request.form['transaction_id'])
            data['transaction_id_number'] = request.form['transaction_id_number']

            jsonDict['payments'][item] = data
    return jsonify(jsonDict)

@app.route('/payments/<int:payment_id_delete>', methods=['DELETE'])
def delete_payment_by_id(payment_id_delete):
    itemDelete = ''
    for item in jsonDict['payments']:
        if int(jsonDict['payments'][item]['id']) == int(payment_id_delete):
            itemDelete = item
    jsonDict['payments'].pop(itemDelete)
    return jsonify(jsonDict)


if __name__ == "__main__":
    database = DATABASESERVER()
    jsonDict = database.dataJson
    
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=5000, debug=True)
