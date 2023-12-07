"""Seed file sample data"""

from models import  Username, Card, Deck, User_Deck
from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()

    test = Username(username='test')

    db.session.add(test)

    db.session.commit()