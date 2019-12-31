from app import db

class UnibCombos(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    character = db.Column(db.String(15), index=True, nullable=False)
    damage = db.Column(db.Integer, index=True, nullable=False)
    cs = db.Column(db.Boolean, index=True, nullable=False)
    ch = db.Column(db.Boolean, index=True, nullable=False)
    starter = db.Column(db.String(10), index=True, nullable=False)
    meter = db.Column(db.Integer, index=True, nullable=False)

    yt = db.Column(db.String(300), index=True)
    tw = db.Column(db.String(300), index=True)
    bullets = db.Column(db.Integer, index=True)
    enh = db.Column(db.Integer, index=True)