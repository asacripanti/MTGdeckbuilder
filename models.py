from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Username(db.Model):

    __tablename__ = 'usernames'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))

class Card(db.Model):

    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)
    card_type = db.Column(db.String(50))
    color = db.Column(db.String(50))
    cmc = db.Column(db.Integer)
    img_url = db.Column(db.String)


class Deck(db.Model):

    __tablename__ = 'decks'

    id = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(50), nullable=False)


class Deck_Card(db.Model):

    __tablename__ = 'deck_cards'   

    id = db.Column(db.Integer, primary_key=True)
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))      
    

class User_Deck(db.Model):

    __tablename__ = 'user_decks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usernames.id'))
    deck_card_id = db.Column(db.Integer, db.ForeignKey('deck_cards.id'))


def connect_db(app):
    db.app = app
    db.init_app(app)