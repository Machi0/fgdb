from app.api import bp
from flask import jsonify, request
from app.models import UnibCombos
from app import db
from app.api.errors import bad_request

@bp.route('/unib/combos', methods=['GET'])
def get_combo():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = UnibCombos.to_collection_dict(UnibCombos.query, page, per_page, 'api.unib.get_combo')
    return jsonify(data)

@bp.route('unib/combos', methods=['POST'])
def post_combo():
    data = request.get_json() or {}

    if 'character' not in data or 'ver' not in data or 'damage' not in data or\
        'cs' not in data or 'ch' not in data or 'starter' not in data or\
        'meter' not in data:
            return bad_request("Fields missing data")
    
    combo = UnibCombos()
    combo.from_dict(data)
    db.session.add(combo)
    db.session.commit()

    response = jsonify(combo.to_dict())
    response.status_code = 201
    return response