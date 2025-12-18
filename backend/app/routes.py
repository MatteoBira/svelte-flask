from flask import Blueprint, jsonify, request
from app.models import get_all_todos, add_todo, update_todo, delete_todo

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(get_all_todos())

@api.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = add_todo(data['title'])
    return jsonify(new_todo), 201

@api.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo_route(todo_id):
    data = request.json
    updated = update_todo(todo_id, data)
    if updated:
        return jsonify(updated)
    return jsonify({"error": "Todo not found"}), 404

@api.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_route(todo_id):
    delete_todo(todo_id)
    return '', 204
