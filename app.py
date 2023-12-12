"""MTG deck builder APP"""

from flask import Flask, render_template, request, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import CardSearchForm, RegisterForm, CreateDeckForm
from models import db, Username, connect_db, User_Deck, Deck
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


    if form.validate_on_submit():
        deck_name = form.name.data

        new_deck = Deck(deck_name=deck_name)

        db.session.add(new_deck)

        db.session.commit()

    return render_template('home.html', form=form)


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

            session['logged_in'] = True
            session['username'] = username

        finally:
            db.session.close()

    return render_template('register.html', form=form)    


@app.route('/deck', methods=['GET', 'POST'])
def deck_display():
    """Overview of deck"""   
    form = CardSearchForm()

    if request.method == 'POST':
        print("Form submitted!")
        print(f"Form data: {request.form}")

    

    # Render the home template with the form
    return render_template('Deck.html', form=form)
    
   

@app.route('/search', methods=['GET', 'POST'])
def card_search():
    """Route that sends user to form for card search"""
    
    form = CardSearchForm()

    if session.get('logged_in'):
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
                    # Add more fields as needed

            except requests.exceptions.RequestException as e:
                print(f"Error making API request: {e}")
            # Additional actions can be added here

        # Render the home template with the form
        return render_template('Deck.html', form=form, card_data=card_data)
    
    # If the user is not logged in, redirect to the register page
    else:
        return redirect(url_for('register_user'))



    
        




if __name__ == '__main__':
    app.run(debug=True)


