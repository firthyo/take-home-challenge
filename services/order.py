from flask import Flask, jsonify, request

from utils.convert_helper import convert_xml_to_json, convert_csv_to_json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_TAB'] = True

# BONUS Pagination
def paginate_data(data, per_page, page):
    total_data = len(data)
    start_index = (page - 1) * per_page
    end_index = start_index + per_page

    paginated_data = data[start_index:end_index]

    response = {
        'page': page,
        'per_page': per_page,
        'total_data': total_data,
        'data': paginated_data
    }

    return response

@app.route('/user/<user_id>/orders/<int:page>', methods=['GET'])
def user_orders(user_id, page):
    data_dict = convert_xml_to_json('../data/orders.xml')
    orders = data_dict['root']['orders']['order']
    user_orders = [order for order in orders if order['user_id'] == user_id]
    per_page = int(request.args.get('per_page', 10))
    paginated_user_orders = paginate_data(user_orders, per_page, page)

    return jsonify(paginated_user_orders)

@app.route('/user/<user_id>/order_items/<int:page>', methods=['GET'])
def get_order_items(user_id, page):
    data = convert_xml_to_json("../data/orders.xml")['root']
    item_data = convert_csv_to_json("../data/items.csv")
    user_order_indices = [i for i, order in enumerate(data['orders']['order']) if order['user_id'] == user_id]

    if not user_order_indices:
        return jsonify({'message': 'No orders found for this user.'}), 404

    user_order_items = []
    for index in user_order_indices:
        items = data['orders']['items'][index]['item']
        if type(items) == list:
            for item in items:
                item_id = item['id']
                if item_id in item_data:
                    user_order_items.append(item_data[item_id])
        else:
            item_id = items['id']
            if item_id in item_data:
                user_order_items.append(item_data[item_id])

    per_page = int(request.args.get('per_page', 10))
    paginated_order_items = paginate_data(user_order_items, per_page, page)

    return jsonify(paginated_order_items)



if __name__ == '__main__':
    app.run(port=8000, debug=True)
