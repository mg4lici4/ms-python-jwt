from flask import Flask
from flask_jwt_extended import JWTManager

# Crear isntancia de la clase Flask
app = Flask(__name__)

#Configuracicón del JWT
app.config['JWT_SECRET_KEY'] = 'super-secreto'
jwt = JWTManager(app)

# Importar las rutas
from app import routes