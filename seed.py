"""Seed file sample data"""

from models import  Usernames, Cards, Decks, User_Decks
from app import app, db

with app.app_context():
    db.drop_all()
    db.create_all()

    test = Usernames(username='test')

    db.session.add(test)

    db.session.commit()