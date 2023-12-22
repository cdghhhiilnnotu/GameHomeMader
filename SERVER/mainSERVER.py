from flask import Flask, request, jsonify, send_file
from Data.mainDATA import jsonDict

app = Flask(__name__)

@app.route('/get_png')
def get_png():
    # Đường dẫn đến file PNG
    png_path = 'icon-app-user.png'
    # Gửi file về client
    return send_file(png_path, mimetype='image/png')

# ALL ROUTE
@app.route('/', methods=['GET'])
def get_all():
    return jsonify(jsonDict)

# GAMES ROUTE
@app.route('/games', methods=['GET'])
def get_all_games():
    return jsonify(jsonDict['games'])

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
    if int(request.form['id']) not in list(map(lambda data: data["id"], jsonDict['users'].values())):
        data = {}
        data['email'] = request.form['email']
        data['id'] = int(request.form['id'])
        data['name'] = request.form['name']
        data['password'] = request.form['password']

        jsonDict['users'][f'user{len(jsonDict["users"])}'] = data

    return jsonify(jsonDict), 201

@app.route('/users/<int:user_id_put>', methods=['PUT'])
def put_user_by_id(user_id_put):
    for item in jsonDict['users']:
        if int(jsonDict['users'][item]['id']) == int(user_id_put):
            data = {}
            data['email'] = request.form['email']
            data['id'] = int(user_id_put)
            data['name'] = request.form['name']
            data['password'] = request.form['password']

            jsonDict['users'][item] = data
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
    return jsonDict['transactions']

@app.route('/transactions/<int:transaction_id>', methods=['GET'])
def get_transaction_id(transaction_id):
    return jsonDict['transactions'][f'transaction{transaction_id-1}']

@app.route('/transactions', methods=['POST'])
def post_transaction():
    if int(request.form['id']) not in list(map(lambda data: data["id"], jsonDict['transactions'].values())):
        data = {}
        data['created_at'] = request.form['created_at']
        data['game_id'] = int(request.form['game_id'])
        data['id'] = int(request.form['id'])
        data['price'] = float(request.form['price'])
        data['status'] = request.form['status']
        data['updated_at'] = request.form['updated_at']
        data['user_id'] = int(request.form['user_id'])

        jsonDict['transactions'][f'transaction{len(jsonDict["transactions"])}'] = data

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
    itemDelete = ''
    for item in jsonDict['transactions']:
        if int(jsonDict['transactions'][item]['id']) == int(transaction_id_delete):
            itemDelete = item
    jsonDict['transactions'].pop(itemDelete)
    return jsonify(jsonDict)

# PAYMENTS ROUTE
@app.route('/payments', methods=['GET'])
def get_all_payments():
    return jsonDict['payments']

@app.route('/payments/<int:payment_id>', methods=['GET'])
def get_payment_id(payment_id):
    return jsonDict['payments'][f'payment{payment_id-1}']

@app.route('/payments', methods=['POST'])
def post_payment():
    if int(request.form['id']) not in list(map(lambda data: data["id"], jsonDict['payments'].values())):
        data = {}
        data['amount'] = float(request.form['amount'])
        data['id'] = int(request.form['id'])
        data['payment_method'] = request.form['payment_method']
        data['transaction_id'] = float(request.form['transaction_id'])
        data['transaction_id_number'] = request.form['transaction_id_number']

        jsonDict['payments'][f'payment{len(jsonDict["payments"])}'] = data

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
    app.run(host='0.0.0.0', port=5000, debug=True)
