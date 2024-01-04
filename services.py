"""Functions defined"""
from models import db, Username

def get_user_id(username):
    user = Username.query.filter_by(username=username).first()
    if user:
        print(f"User found with username '{username}'. User ID: {user.id}")
        return user.id
    else:
        print(f"No user found with username '{username}'.")
        return None