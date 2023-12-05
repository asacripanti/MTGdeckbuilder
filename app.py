"""MTG deck builder APP"""

from flask import Flask, render_template, request, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import CardSearchForm, RegisterForm
from models import db, Usernames

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/deck_builder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    """Home page with card search form"""

    form = CardSearchForm()

    if session.get('logged_in'):
        # Check if the form is submitted
        if form.validate_on_submit():
            # Access the form data using form.name.data
            card_name = form.name.data
            # Perform the API request using card_name
            print(f"Form submitted with card name: {card_name}")
            # Additional actions can be added here

        # Render the home template with the form
        return render_template('home.html', form=form)
    
    # If the user is not logged in, redirect to the register page
    else:
        return redirect(url_for('register_user'))


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Create username or log in if not signed in"""

    form = RegisterForm()

    if form.validate_on_submit():
        try:
            username = form.username.data

            new_user = Usernames(username=username)

            db.session.add(new_user)

            db.session.commit()

            session['logged_in'] = True
            session['username'] = username

        finally:
            db.session.close()

    return render_template('register.html', form=form)    
        




if __name__ == '__main__':
    app.run(debug=True)


