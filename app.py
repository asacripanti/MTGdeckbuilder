"""MTG deck builder APP"""

from flask import Flask, render_template, request, url_for, session, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import CardSearchForm, RegisterForm, CreateDeckForm, LoginForm
from models import db, Username, connect_db, User_Deck, Deck, Card, Deck_Card
from services import get_user_id
import requests 
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/deck_builder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

migrate = Migrate(app, db)

connect_db(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    """homepage two"""

    form = CreateDeckForm()

    if 'logged_in' not in session:
        return redirect(url_for('register_user'))

    username = session.get('username')
    user_id = session.get('user_id')    
    deck_id = None


    if form.validate_on_submit():

        deck_name = form.name.data

        new_deck = Deck(deck_name=deck_name)

        db.session.add(new_deck)
        db.session.commit()

        deck_id = new_deck.id

        user_deck = User_Deck(user_id=user_id, deck_id=deck_id)

        db.session.add(user_deck)
        db.session.commit()

    user_decks_query = (
        db.session.query(User_Deck)
        .join(Deck, User_Deck.deck_id == Deck.id)
        .filter(User_Deck.user_id == user_id)
    )    
    user_decks_result = user_decks_query.all()
    print(str(user_decks_query))
    deck_names = [user_deck.deck.deck_name for user_deck in user_decks_query]
    print("Deck Names:", deck_names)
            
    return render_template('home.html', form=form, username=username, user_id=user_id, deck_id=deck_id, deck_names=deck_names, user_deck_result=user_decks_result)


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Create username or log in if not signed in"""

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            username = form.username.data
            new_user = Username(username=username)

            db.session.add(new_user)
            db.session.commit()

            user_id = new_user.id

            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user_id

        finally:
                db.session.close()
                return redirect(url_for('home_page'))

    return render_template('register.html', form=form) 
   

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Allows user to login"""

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        user_id = get_user_id(username)
        print(f"here is your username {username}")

        if user_id is not None:
            session['logged_in'] = True
            session['username'] = username
            session['user_id'] = user_id
            return redirect(url_for('home_page'))
        else:
            flash('Invalid username. Please try again.', 'error')
            
    return render_template('login.html', form=form)    



@app.route('/deck/<int:deck_id>')
def deck_display(deck_id):
    """Overview of deck"""  
    # Render the home template with the form

    session['deck_id'] = deck_id
    user_id = session.get('user_id')

    user_deck = User_Deck.query.filter_by(user_id=user_id, deck_id=deck_id).first()

    if user_deck:
        deck_cards = Deck_Card.query.filter_by(user_deck_id=user_deck.id).all()
        

    return render_template('Deck.html', deck_cards=deck_cards)
    
   

@app.route('/search', methods=['GET', 'POST'])
def card_search():
    """Route that sends user to form for card search"""
    
    form = CardSearchForm()

    if session.get('logged_in'):
        card_data = []
        # Check if the form is submitted
        if form.validate_on_submit():
            # Access the form data using form.name.data
            card_name = form.name.data
            # Perform the API request using card_name
            api_url = f'https://api.magicthegathering.io/v1/cards?name={card_name}'
            params = {'name': card_name}
            print(f"Form submitted with card name: {card_name}")

            try:
                response = requests.get(api_url, params=params)
                response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
                card_data = response.json().get('cards', [])

                for card in card_data:
                    print(f"Card Name: {card.get('name')}")
                    print(f"Card Type: {card.get('type')}")
                    print(f"Mana Cost: {card.get('manaCost')}")
                    print(f"Color: {card.get('colorIdentity')}")
                    print(card_data)
                    # Add more fields as needed

            except requests.exceptions.RequestException as e:
                print(f"Error making API request: {e}")
            # Additional actions can be added here

        # Render the home template with the form
        return render_template('search.html', form=form, card_data=card_data)
    
    # If the user is not logged in, redirect to the register page
    else:
        return redirect(url_for('register_user'))


@app.route('/add_card', methods=['POST'])
def add_card():
    """route that pushes data from JS to DB"""        
    card_data = request.json

    new_card = Card(
        card_name=card_data['name'],
        card_type=card_data['type'],
        color=card_data['colors'],
        cmc=int(card_data['cmc']),
        img_url=card_data['img']
    )
    db.session.add(new_card)
    db.session.commit()

    user_id = session['user_id']

    deck_id = session.get('deck_id')

    user_deck = User_Deck.query.filter_by(user_id=user_id, deck_id=deck_id).first()
    deck_card = Deck_Card(user_deck_id=user_deck.id, card_id=new_card.id)

    db.session.add(deck_card)
    db.session.commit()

    return jsonify({'message': 'Card added successfully'})


@app.route('/logout')
def logout():
    """Clears session and logs user out"""

    session.clear()
    return redirect(url_for('home_page'))        



    
        




if __name__ == '__main__':
    app.run(debug=True)


