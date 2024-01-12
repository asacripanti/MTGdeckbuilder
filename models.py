from sqlalchemy import func
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
    user_deck_id = db.Column(db.Integer, db.ForeignKey('user_decks.id'))
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'))      

    card = db.relationship('Card', backref='deck_cards')
    user_deck = db.relationship('User_Deck', backref='deck_cards')
    

class User_Deck(db.Model):

    __tablename__ = 'user_decks'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usernames.id'))
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))
    


    user = db.relationship('Username', foreign_keys=[user_id], backref='user_decks')
    deck = db.relationship('Deck', foreign_keys=[deck_id], backref='user_decks')

    @property
    def card_count(self):
        return Deck_Card.query.filter_by(user_deck_id=self.id).count()

    @classmethod
    def get_decks_with_card_count(cls):
        return cls.query.join(Deck_Card).group_by(cls.id).add_columns(func.count(Deck_Card.id).label('card_count')).all()



def connect_db(app):
    db.app = app
    db.init_app(app)