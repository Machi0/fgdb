from flask import current_app
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
    ms = db.Column(db.Boolean, index=True, nullable=False) 
    starter = db.Column(db.String(10), index=True, nullable=False) 
    meter = db.Column(db.Integer, index=True, nullable=False)
    
    yt = db.Column(db.String(300), index=True)
    tw = db.Column(db.String(300), index=True)
    bullets = db.Column(db.Integer, index=True)
    enh = db.Column(db.Integer, index=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'character': self.character,
            'ver': self.ver,
            'damage': self.damage,
            'cs': self.cs,
            'ch': self.ch,
            'ms': self.ms,
            'starter': self.starter,
            'meter': self.meter
        }

        if self.character == "eltnum":
            data['bullets'] = self.bullets
            data['enh'] = self.enh
        elif self.character == "wagner":
            pass

        if self.yt != None:
            data['yt'] = self.yt
        elif self.tw != None:
            data['tw'] = self.tw
    
        return data
    
    def from_dict(self, data):
        fields = [
            'character', 'ver', 'damage', 'cs', 'ch',
            'starter', 'meter', 'ms', 'yt', 'tw', 'bullets',
            'enh'
        ]

        for field in fields:
            if field in data:
                setattr(self, field, data[field])
