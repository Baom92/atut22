from config import db


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False, unique=True)
    image = db.Column(db.String(255))
    description = db.Column(db.Text)
    note = db.Column(db.String(80))
