## Put and delete -http verbs
## working with api's -- jsoon 

from flask import Flask, jsonify, request

app = Flask(__name__)

## Initial data in my to do list 
items = [
    {'id': 1, 'task': 'Buy groceries'},
    {'id': 2, 'task': 'Clean the house'},
    {'id': 3, 'task': 'Finish homework'}
]

@app.route("/")
def home():
    return "Welcome to the To-Do List!"

## Get : Retrieve all items in the to-do list
@app.route("/items", methods=['GET'])
def get_items():
    return jsonify(items)

## get : Retrieve a specific item by id
@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

## Post : Create a new item in the to-do list
@app.route("/items", methods=['POST'])
def create_item():
    new_item = request.get_json()
    new_item['id'] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

## Put : Update an existing item in the to-do list
@app.route("/items/<int:item_id>", methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        updated_data = request.get_json()
        item.update(updated_data)
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    
## Delete : Remove an item from the to-do list
@app.route("/items/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'})



if __name__ == '__main__':
    app.run(debug=True)