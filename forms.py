from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired

class CardSearchForm(FlaskForm):
    """Form that allows user to search for cards"""

    name = StringField("Card Name", validators=[InputRequired()])

class LoginForm(FlaskForm):
    """Form that allows user to login with username"""

    username = StringField("Username", validators=[InputRequired()])    

class RegisterForm(FlaskForm):
    """Form that allows user to create a username"""

    username = StringField("Username", validators=[InputRequired()])    

