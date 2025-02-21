from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
import datetime

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

@api.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()

    if not body:
        raise APIException("You need to specify the request body as a JSON object", status_code=400)
    if 'email' not in body:
        raise APIException("You need to specify the email", status_code=400)
    if 'password' not in body:
        raise APIException("You need to specify the password", status_code=400)

    user = User(email=body['email'], password=body['password'], is_active=True)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created successfully"}), 201

@api.route('/login', methods=['POST'])
def login():
    body = request.get_json()

    if not body:
        raise APIException("You need to specify the request body as a JSON object", status_code=400)
    if 'email' not in body:
        raise APIException("You need to specify the email", status_code=400)
    if 'password' not in body:
        raise APIException("You need to specify the password", status_code=400)

    user = User.query.filter_by(email=body['email']).first()
    if not user or user.password != body['password']:
        raise APIException("Invalid email or password", status_code=401)

    expiration = datetime.timedelta(hours=48)  # Duración de 48 horas
    access_token = create_access_token(identity=str(user.id), expires_delta=expiration)

    return jsonify({"token": access_token}), 200

@api.route('/users', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.all()
    user_list = [{"id": user.id, "email": user.email, "is_active": user.is_active, "is_admin": user.is_admin} for user in users]
    return jsonify(user_list), 200
200

@api.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = User.query.get(id)
    
    if not user:
        raise APIException("User not found", status_code=404)
    
    body = request.get_json()

    if not body:
        raise APIException("You need to specify the request body as a JSON object", status_code=400)
    
    if 'email' in body:
        user.email = body['email']
    if 'password' in body:
        user.password = body['password']
    
    db.session.commit()
    
    return jsonify({"message": "User information updated successfully"}), 200

@api.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get(id)
    
    if not user:
        raise APIException("User not found", status_code=404)
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({"message": f"User with id {id} deleted successfully"}), 200
