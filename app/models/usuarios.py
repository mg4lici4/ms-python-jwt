# Simulación de una base de datos de usuarios

usuarios = {
    'usuario1': {'username': 'usuario1', 'password': 'contraseña1'},
    'usuario2': {'username': 'usuario2', 'password': 'contraseña2'}
}

def obtener_usuario(username):
    """
    Obtiene un usuario por su nombre de usuario.
    """
    return usuarios.get(username)