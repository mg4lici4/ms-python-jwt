from flask import Flask, jsonify, request
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)
from app import app
from app.models import obtener_usuario

# Ruta para autenticación y generación de JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Verificar credenciales
    user = obtener_usuario(username)
    if user and user['password'] == password:
        # Crear un token JWT
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Usuario o contraseña incorrectos"}), 401

# Ruta protegida que requiere un JWT válido
@app.route('/protegido', methods=['GET'])
@jwt_required()
def protegido():
    # Obtener la identidad del usuario desde el token
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200