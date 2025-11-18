import data
from models import Usuario
from flask import Blueprint, jsonify, request

routes = Blueprint('routes', __name__)

@routes.route('/')
def inicio():
    return "Bienvenido a la API de usuarios"

#Ruta para mostrar todos los usuarios
@routes.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = data.leer_tabla_usuarios(data.conexion_db())
    return jsonify([u.to_dict() for u in usuarios])

#Ruta para buscar usuario por nombre
@routes.route('/usuarios/buscar/<nombre>', methods=['GET'])
def buscar_usuario(nombre):
    usuarios = data.buscar_por_nombre(data.conexion_db(), nombre)
    return jsonify([u.to_dict() for u in usuarios])

#Ruta para actualizar usuario por ID
@routes.route('/usuarios/actualizar/<int:id>', methods=['GET'])
def actualizar_usuario(id):
    usuario = data.actualizar_usuario_por_id(data.conexion_db(), id)
    return jsonify(usuario.to_dict()) if usuario else ("Usuario no encontrado", 404)

#Ruta para agregar un nuevo usuario
@routes.route('/usuarios', methods=['POST'])
def agregar_usuario():
    datos = request.get_json()
    nuevo = Usuario(None, datos["nombre"], datos["cedula"], datos["correo_electronico"], datos["telefono"], datos["fecha_nacimiento"])
    data.insertar_usuario(data.conexion_db(), nuevo)
    return jsonify(nuevo.to_dict()), 201

#Ruta para borrar un usuario por ID
@routes.route('/usuarios/<int:id>', methods=['DELETE'])
def borrar_usuario(id):
    data.borrar_usuario_por_id(data.conexion_db(), id)
    return ("Usuario eliminado", 204)

#Ruta para editar un usuario por ID
@routes.route('/usuarios/<int:id>', methods=['PUT'])
def editar_usuario(id):
    datos = request.get_json()
    usuario = data.actualizar_usuario_por_id(data.conexion_db(), id)
    if usuario:
        usuario.nombre = datos.get("nombre", usuario.nombre)
        usuario.cedula = datos.get("cedula", usuario.cedula)
        usuario.correo_electronico = datos.get("correo_electronico", usuario.correo_electronico)
        usuario.telefono = datos.get("telefono", usuario.telefono)
        usuario.fecha_nacimiento = datos.get("fecha_nacimiento", usuario.fecha_nacimiento)
        return jsonify(usuario.to_dict())
    return ("Usuario no encontrado", 404)