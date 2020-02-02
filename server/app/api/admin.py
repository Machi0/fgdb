from app.api import bp
from app.models import Admin
from app import db
from flask import jsonify, request


@bp.route('/matrix/', methods=['POST'])
def checkCreds():
    data = request.get_json() or {}

    if 'username' not in data or 'password' not in data:
        return jsonify({'auth': 'false'})

    admin = Admin.query.get(1)

    if data['username'] == admin.username and admin.check_password(data['password']):
        return jsonify({'auth': 'true'})
    else:
        return jsonify({'auth': 'false'})
