"""MTG deck builder APP"""

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import CardSearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/deck_builder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    """Home page with card search form"""

    form = CardSearchForm()

    if form.validate_on_submit():
        # Access the form data using form.name.data
        card_name = form.name.data
        # Perform the API request using card_name
        print(f"Form submitted with card name: {card_name}")
        # Additional actions can be added here

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


