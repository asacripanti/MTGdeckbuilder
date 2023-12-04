from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    deck_id = db.Column(db.Integer, db.ForeignKey('Deck.id'))

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)
    card_type = db.Column(db.String(50))
    color = db.Column(db.String(50))
    cmc = db.Column(db.Integer)
    img_url = db.Column(db.String)


class Deck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(50), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('card.id'))
    card_name = db.Column(db.String(50), db.ForeignKey('card.card_name'))     
    card_color = db.Column(db.String(50), db.ForeignKey('card.color'))
    card_type = db.Column(db.String(50), db.ForeignKey('card.card_type'))
    card_cmc = db.Column(db.Integer, db.ForeignKey('card.cmc'))
    card_img = db.Column(db.String, db.ForeignKey('card.img_url'))