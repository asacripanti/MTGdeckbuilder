from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Usernames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)
    card_type = db.Column(db.String(50))
    color = db.Column(db.String(50))
    cmc = db.Column(db.Integer)
    img_url = db.Column(db.String)


class Decks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(50), nullable=False)
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))

class User_Decks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usernames.id'))
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))    