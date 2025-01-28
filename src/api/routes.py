"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, Users, Hosts, Players, Tournaments, Matches, Participants, Match_participants, Teams
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

# /////////////////////////////////////////USER/////////////////////////////////////////

@api.route('/signup', methods=['POST'])
def register():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    player = request.json.get ('player', None)
   

    if not email or not password or not player:
        return jsonify({'msg': 'Todos los campos son necesarios'}), 400


    exist = Users.query.filter_by(email=email).first()
    if exist: 
        return jsonify({'success': False, 'msg': 'El correo electronico ya existe'}), 400
    
    hashed_password = generate_password_hash(password)
    print(hashed_password)
    new_user = Users(email=email, password=hashed_password, player=player)

    if player: 
        new_player = Players()
        db.session.add(new_player)
        db.session.flush()
        new_user.player_id = new_player.id
        db.session.add(new_user)
        db.session.commit()
        token = create_access_token(identity=str(new_user.id))
        return jsonify({'user_info': new_user.serialize(), 'player_info': new_player.serialize(), 'token': token}), 200

    if not player: 
        new_host = Hosts()
        db.session.add(new_host)
        db.session.flush()
        new_user.host_id = new_host.id
        db.session.add(new_user)
        db.session.commit()
        token = create_access_token(identity=str(new_user.id))
        return jsonify({'user_info': new_user.serialize(), 'host_info': new_host.serialize(), 'token': token}), 200


@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    
    if not email or not password:
        return jsonify({'msg': 'Email y contraseña son obligatorios'}), 400
    
    user = Users.query.filter_by(email=email).first()
    
    if not user:
        return jsonify({'msg': 'Usuario no encontrado'}), 404
    
    if not check_password_hash (user.password, password):
        return jsonify ({'msg': 'email/contraseña incorrectos'}), 404

    
    token = create_access_token(identity=str(user.id))
    return jsonify({'msg': 'ok', 'token': token}), 200

@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    identity = get_jwt_identity()
    users = Users.query.get(identity)   
    if users: 
        print(users.serialize()) 
        return jsonify({'success': True, 'msg': 'OK', 'user': users.serialize()})
    return jsonify({'success': False, 'msg': 'Token erroneo'})

# /////////////////////////////////////////HOST/////////////////////////////////////////

@api.route('/host/profile', methods=['GET'])    # Mostrar lista de perfiles de todos los hosts
def all_host_profile():
    try:
        all_hosts = Hosts.query.all()

        if not all_hosts:
            return jsonify({'msg': 'Hosts no encontrados'}), 404
        
        serialized_hosts = [host.serialize() for host in all_hosts]

        return jsonify({'hosts': serialized_hosts}), 200
    
    except Exception as e:
        return jsonify({'msg': 'Ocurrió un error al obtener los hosts', 'error': str(e)}), 500


@api.route('/host/profile/<int:id>', methods=['GET'])   # Mostrar el perfil del host seleccionado
def one_host_profile(id):
    try:
        host = Hosts.query.get(id)   
        if not host:
            return jsonify({'msg': 'Host no encontrado'}), 404 
        
        return jsonify({'host': host.serialize()}), 200
    
    except Exception as e:
        return jsonify({'msg': 'Ocurrió un error al obtener los hosts', 'error': str(e)}), 500


@api.route('/host/profile/<int:id>', methods=['PUT'])    #Editar el perfil del host seleccionado
def edit_host_profile(id):
    try:
        data = request.json

        host = Hosts.query.get(id)
        
        if not host:
            return jsonify({'msg': 'Host no encontrado'}), 404
 
        host.name = data.get('name', host.name)
        host.address = data.get('address', host.address)
        host.court_type = data.get('court_type', host.court_type)
        host.tournament_id = data.get('tournament_id', host.tournament_id)

        db.session.commit()

        return jsonify({'msg': 'Host actualizado con éxito', 'host': host.serialize()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# /////////////////////////////////////////TOURNAMENT/////////////////////////////////////////

@api.route('/tournaments', methods=['POST'])    # Crear un torneo
def create_tournament():
    
    data = request.json

    name = data.get('name', None)
    type = data.get('type', None)
    inscription_fee = data.get('inscription_fee', None)
    rating = data.get('rating', None)
    schedule = data.get('schedule', None)
    award = data.get('award', None)
    image = data.get('image', None)
    
    if not name or not type or not inscription_fee or not rating or not schedule or not award or not image:
        return jsonify({'msg': 'Completa los datos obligatorios'}), 400
    
    new_tournament = Tournaments(
            name=name,
            type=type,
            inscription_fee=inscription_fee,
            rating=rating,
            schedule=schedule,
            award=award,
            image=image
        )
    db.session.add(new_tournament)
    db.session.commit()

    return jsonify({'msg': 'Torneo creado con éxito', 'tournament': new_tournament.serialize()}), 200
    
@api.route('/tournaments', methods=['GET'])    # Mostrar lista torneos
def all_tournaments():
    try:
        all_tournaments = Tournaments.query.all()

        if not all_tournaments:
            return jsonify({'msg': 'Torneos no encontrados'}), 404
        
        serialized_tournaments = [tournament.serialize() for tournament in all_tournaments]

        return jsonify({'Torneos': serialized_tournaments}), 200
    
    except Exception as e:
        return jsonify({'msg': 'Ocurrió un error al obtener los torneos', 'error': str(e)}), 500
    

@api.route('/tournaments/<int:id>', methods=['GET'])    # Mostrar un torneo
def one_tournament(id):
    try:
        tournament = Tournaments.query.get(id)   
        if not tournament:
            return jsonify({'msg': 'Torneo no encontrado'}), 404 
        
        return jsonify({'Torneo': tournament.serialize()}), 200
    
    except Exception as e:
        return jsonify({'msg': 'Ocurrió un error al obtener el torneo', 'error': str(e)}), 500

@api.route('/tournaments/<int:id>', methods=['PUT'])    #Editar el torneo seleccionado
def edit_tournament(id):
    try:
        data = request.json

        tournament = Tournaments.query.get(id)
        
        if not tournament:
            return jsonify({'msg': 'Torneo no encontrado'}), 404
 
        tournament.name = data.get('name', tournament.name)
        tournament.type = data.get('address', tournament.type)
        tournament.inscription_fee = data.get('court_type', tournament.inscription_fee)
        tournament.rating = data.get('tournament_id', tournament.rating)
        tournament.schedule = data.get('address', tournament.schedule)
        tournament.award = data.get('court_type', tournament.award)
        tournament.tournament_winner = data.get('tournament_id', tournament.tournament_winner)
        tournament.image = data.get('tournament_id', tournament.image)

        db.session.commit()

        return jsonify({'msg': 'Torneo actualizado con éxito', 'Torneo': tournament.serialize()}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@api.route('/tournaments/<int:id>', methods=['DELETE'])
def delete_tournament(id):

    data = Tournaments.query.get(id)

    db.session.delete(data)
    db.session.commit()

    return jsonify({"msg": "Torneo eliminado con id " + str(id)}), 200