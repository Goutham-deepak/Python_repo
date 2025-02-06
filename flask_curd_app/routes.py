# # routes.py
# from flask import Blueprint, request, jsonify
# from database import db, User

# routes = Blueprint('routes', __name__)

# # Create a new user (POST)
# @routes.route('/users', methods=['POST'])
# def create_user():
#     data = request.json
#     new_user = User(name=data['name'], email=data['email'])
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user.to_dict()), 201

# # Get all users (GET)
# @routes.route('/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.to_dict() for user in users])

# # Get a single user by ID (GET)
# @routes.route('/users/<int:user_id>', methods=['GET'])
# def get_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({"error": "User not found"}), 404
#     return jsonify(user.to_dict())

# # Update a user (PUT)
# @routes.route('/users/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({"error": "User not found"}), 404

#     data = request.json
#     user.name = data.get('name', user.name)
#     user.email = data.get('email', user.email)

#     db.session.commit()
#     return jsonify(user.to_dict())

# # Delete a user (DELETE)
# @routes.route('/users/<int:user_id>', methods=['DELETE'])
# def delete_user(user_id):
#     user = User.query.get(user_id)
#     if not user:
#         return jsonify({"error": "User not found"}), 404

#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({"message": "User deleted successfully"})
