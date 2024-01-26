from flask import Flask, request, jsonify, abort
from Errores_HTTP import *

app = Flask(__name__)

@app.route('/test')
def main():
    status = request.headers.get('status')
    if status == "200":
        return success()
    elif status == "201":
        return created()
    elif status == "400":
        return bad_request_error()
    elif status == "401":
        return unauthorized_error()
    elif status == "403":
        return forbidden_error()
    elif status == "404":
        return not_found_error()
    elif status == "405":
        return not_allowed_error()
    elif status == "408":
        return request_timeout()
    elif status == "429":
        return too_many_request()
    else:
        return internal_server_error()

if __name__ == '__main__':
    app.run(debug=False)