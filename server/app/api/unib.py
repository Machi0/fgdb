from app.api import bp
from flask import jsonify, request
from app.models import UnibCombos
from app import db
from app.api.errors import bad_request

@bp.route('/unib/combos/', methods=['GET'])
def get_combo():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 24, type=int), 100)
    query = UnibCombos.get_query(UnibCombos)
    data = UnibCombos.to_collection_dict(query, page, per_page, 'api.unib.get_combo')
    return jsonify(data)

@bp.route('unib/combos/', methods=['POST'])
def post_combo():
    data = request.get_json() or {}

    if 'character' not in data or 'ver' not in data or 'damage' not in data or\
        'cs' not in data or 'ch' not in data or 'starter' not in data or\
        'meter' not in data or 'pos' not in data:
            return bad_request("Fields missing data")
    
    if data['character'] == 'Eltnum' and ('bullets' not in data or 'enh' not in data):
        return bad_request("Missing Eltnum fields")
    elif data['character'] == 'Wagner' and ('wSword' not in data or 'wShield' not in data):
        return bad_request("Missing Wagner fields")
    elif data['character'] == 'Chaos' and 'azhi' not in data:
        return bad_request("Missing Chaos fields")
    
    if ('tw' not in data and 'yt' not in data) or ('tw' in data and 'yt' in data):
        return bad_request("Missing URL")

    combo = UnibCombos()
    combo.from_dict(data)
    db.session.add(combo)
    db.session.commit()

    response = jsonify(combo.to_dict())
    response.status_code = 201
    return response

@bp.route('unib/combos/', methods=['PUT'])
def flag_combo():
    data = request.get_json() or {}
    combo = UnibCombos()

    setattr(UnibCombos.query.get(data['id']), 'flag', data['flag'])

    db.session.commit()

    response = jsonify({})
    response.status_code = 201
    return response
