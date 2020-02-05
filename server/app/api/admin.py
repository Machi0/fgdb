from app.api import bp
from app.models import Admin
from app import db
from flask import jsonify, request, g
from flask_httpauth import HTTPBasicAuth
from app.api.errors import error_response
from flask_httpauth import HTTPTokenAuth
from app.models import UnibCombos



basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    user = Admin.query.filter_by(username=username).first()
    if user is None:
        return False
    g.current_user = user
    return user.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)

@token_auth.verify_token
def verify_token(token):
    g.current_user = Admin.check_token(token) if token else None
    return g.current_user is not None

@token_auth.error_handler
def token_auth_error():
    return error_response(401)

@bp.route('/matrix/', methods=['POST'])
@basic_auth.login_required
def checkCreds():
    token = g.current_user.get_token()
    db.session.commit()
    return jsonify({'token': token, 'auth': 'true'})    

@bp.route('/admin/<post_id>', methods=['DELETE'])
@token_auth.login_required
def deletePost(post_id):
    UnibCombos.query.filter_by(id=post_id).delete()
    db.session.commit()

    response = jsonify({})
    response.status_code = 201
    return response

@bp.route('/admin/', methods=['PUT'])
@token_auth.login_required
def editPost():
    data = request.get_json() or {}
    Admin.edit(UnibCombos, data)

    db.session.commit()

    response = jsonify({})
    response.status_code = 201
    return response

@bp.route('/admin/', methods=['GET'])
@token_auth.login_required
def getPosts():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 24, type=int), 100)
    query = Admin.get_query(UnibCombos)
    data = UnibCombos.to_collection_dict(query, page, per_page, 'api.unib.get_combo')
    return jsonify(data)