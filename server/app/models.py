from flask import current_app, request
from app import db

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, end, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            }
        }
        
        return data

class UnibCombos(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 

    character = db.Column(db.String(15), index=True, nullable=False) 
    ver = db.Column(db.String(10), index=True, nullable=False) 
    damage = db.Column(db.Integer, index=True, nullable=False) 
    cs = db.Column(db.Boolean, index=True, nullable=False) 
    ch = db.Column(db.Boolean, index=True, nullable=False)
    pos = db.Column(db.String(10), index=True, nullable=False) 
    starter = db.Column(db.String(10), index=True, nullable=False) 
    meter = db.Column(db.Integer, index=True, nullable=False)
    
    yt = db.Column(db.String(300), index=True)
    tw = db.Column(db.String(300), index=True)
    bullets = db.Column(db.Integer, index=True)
    enh = db.Column(db.Integer, index=True)
    wSword = db.Column(db.Boolean, index=True)
    wShield = db.Column(db.Boolean, index=True)
    azhi = db.Column(db.Boolean, index=True)

    notation = db.Column(db.String(140))
    desc = db.Column(db.String(140))

    def to_dict(self):
        data = {
            'id': self.id,
            'character': self.character,
            'ver': self.ver,
            'damage': self.damage,
            'cs': self.cs,
            'ch': self.ch,
            'pos': self.pos,
            'starter': self.starter,
            'meter': self.meter
        }

        if self.character == "Eltnum":
            data['bullets'] = self.bullets
            data['enh'] = self.enh
        elif self.character == "Wagner":
            data['wSword'] = self.wSword
            data['wShield'] = self.wShield
        elif self.character == "Chaos":
            data['azhi'] = self.azhi

        if self.yt != None:
            data['yt'] = self.yt
        elif self.tw != None:
            data['tw'] = self.tw
        
        if self.desc != None:
            data['desc'] = self.desc
        if self.notation != None:
            data['notation'] = self.notation
    
        return data
    
    def from_dict(self, data):
        fields = [
            'character', 'ver', 'damage', 'cs', 'ch',
            'starter', 'meter', 'pos', 'yt', 'tw', 'bullets',
            'enh', 'wSword', 'wShield', 'azhi', 'notation', 'desc' 
        ]

        for field in fields:
            if field in data:
                setattr(self, field, data[field])
    
    def get_query(self):
        query = self.query

        if request.args.get('char') is not None and request.args.get('char') != 'All':
            query = query.filter_by(character=request.args.get('char'))
        
        if request.args.get('str') is not None and request.args.get('str') != 'All':
            query = query.filter_by(starter=request.args.get('str'))

        if request.args.get('ver') is not None and request.args.get('ver') == 'CLR':
            query = query.filter_by(ver=request.args.get('ver'))
        else:
            query = query.filter_by(ver='ST')
        
        if request.args.get('mtr1') is not None and request.args.get('mtr2') is not None:
            query = query.filter(self.meter>=int(request.args.get('mtr1')))
            query = query.filter(self.meter<=int(request.args.get('mtr2')))

        if request.args.get('flt') == 'Damage':
            query = query.order_by(self.damage.desc())
        
        query = query.order_by(self.id.desc())

        return query
