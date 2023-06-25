from collections import OrderedDict
from flask import Flask, jsonify, request, render_template, render_template_string
import uuid
from utils.user_util import fetch_users, save_users

app = Flask(__name__, template_folder='../templates')
app.config['JSONIFY_PRETTYPRINT_TAB'] = True

@app.route('/', methods=['GET'])
def greeting():
    # return "Hello world"
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_users_list():
    users = fetch_users()
    # BONUS Implement sorting 
    sort_by = request.args.get('sort_by', 'first_name') 
    order = request.args.get('order', 'asc') 
    ordered_users = OrderedDict(sorted(users.items(), key=lambda x: x[1][sort_by]))

    # Reverse the order if descending order is specified
    if order.lower() == 'desc':
        ordered_users = OrderedDict(reversed(list(ordered_users.items())))

    return jsonify(list(ordered_users.values())), 200, {'Content-Type': 'application/json', 'indent': 4}

@app.route('/user/<uuid:id>', methods=['GET'])
def get_user_by_id(id):
    users = fetch_users()
    user = users.get(str(id))
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': f'User ID "{id}" not found'})

@app.route('/user', methods=['POST'])
def create_user():
    users = fetch_users()
    user_data = request.get_json()

    if not user_data:
        return jsonify({'error': 'No data provided'})

    # Validate the required fields in the user data
    required_fields = ['email', 'first_name', 'last_name', 'password']
    for field in required_fields:
        if field not in user_data:
            return jsonify({'error': f'Missing required field: {field}'})

    # Check if the email already exists
    for user in users.values():
        if user['email'] == user_data['email']:
            return jsonify({'error': 'Email already exists'})

    user_id = str(uuid.uuid4())

    # Create a new user object
    new_user = {
        'id': user_id,
        'email': user_data['email'],
        'first_name': user_data['first_name'],
        'last_name': user_data['last_name'],
        'password': user_data['password']
    }

    users[user_id] = new_user
    save_users(users)

    return jsonify(new_user)

# BONUS Pagination
@app.route('/users/paginated/<page>', methods=['GET'])
def get_paginate_users(page):
    users = fetch_users()

    per_page = 10

    try:
        page = int(page)
    except ValueError:
        return jsonify({'error': 'Invalid page number'})

    total_users = len(users)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    ordered_users = OrderedDict(sorted(users.items()))

    user_list = list(ordered_users.values())[start_index:end_index]

    response = {
        'page': page,
        'per_page': per_page,
        'total_users': total_users,
        'users': user_list
    }

    return jsonify(response), 200, {'Content-Type': 'application/json', 'indent': 4}


if __name__ == '__main__':
    app.run(port=8000, debug=True)
