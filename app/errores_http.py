from flask import Flask, jsonify
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
def get_colombia_timestamp():
    zona_bogota = timezone(timedelta(hours=-5))
    hora_bogota = datetime.now(zona_bogota)
    return hora_bogota.strftime("%Y-%m-%d %H:%M:%S")

# Respuesta 200 - Ok
def success():
    response = {
        "status": 200,
        "timestamp": get_colombia_timestamp(),
        "message": "Operacion exitosa"
    }
    return jsonify(response),200

# Respuesta 201 - Created
def created():
    response = {
        "status": 201,
        "timestamp": get_colombia_timestamp(),
        "message": "Recurso creado / actualizado exitosamente"
    }
    return jsonify(response),201

# Error 400 - Bad Request
@app.errorhandler(400)
def bad_request_error(error=""):
    reserror = {
            "status": 400,
            "timestamp": get_colombia_timestamp(),
            "error": "BAD REQUEST - El servidor no puede procesar o reconocer la solicitud, revisa el cache, sintaxis de entrada o cookies del navegador"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),400

# Error 401 - Unauthorized
@app.errorhandler(401)
def unauthorized_error(error=""):
    reserror = {
            "status": 401,
            "timestamp": get_colombia_timestamp(),
            "error": "ACCESS DENIED - Usted no tiene acceso a esta pagina, faltan credenciales"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),401


# Error 403 - Forbidden
@app.errorhandler(403)
def forbidden_error(error=""):
    reserror = {
            "status": 403,
            "timestamp": get_colombia_timestamp(),
            "error": "FORBIDDEN - Acceso restringido a esta pagina, no tiene permiso para acceder"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),403

# Error 404 - Not Found
@app.errorhandler(404)
def not_found_error(error=""):
    reserror = {
            "status": 404,
            "timestamp": get_colombia_timestamp(),
            "error": "NOT FOUND - Recurso o pagina no encontrada, revisar URL en uso"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),404

# Error 405 - Method Not Allowed
@app.errorhandler(405)
def not_allowed_error(error=""):
    reserror = {
            "status": 405,
            "timestamp": get_colombia_timestamp(),
            "error": "METHOD NOT ALLOWED - El metodo HTTP usado es incorrecto o esta deshabilitado"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),405

# Error 408 - Request Timeout
@app.errorhandler(408)
def request_timeout(error=""):
    reserror = {
            "status": 408,
            "timestamp": get_colombia_timestamp(),
            "error": "REQUEST TIMEOUT- Caduco el tiempo de espera para resolver la peticion, revise el estado de su red o espere un momento y vuelva a intentar"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),408

# Error 429 - Too Many Request
@app.errorhandler(429)
def too_many_request(error=""):
    reserror = {
            "status": 429,
            "timestamp": get_colombia_timestamp(),
            "error": "TOO MANY REQUEST- Ha excedido el numero de peticiones aceptadas por el servidor en un tiempo determinado"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),429

# Error 500 - Internal Server Error
@app.errorhandler(500)
def internal_server_error(error=""):
    reserror = {
            "status": 500,
            "timestamp": get_colombia_timestamp(),
            "error": "INTERNAL ERROR SERVER- Hubo un error inesperado en el servidor"}
    if error:
        reserror["message"]=error
    return jsonify(reserror),500
