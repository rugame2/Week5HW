from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,EqualTo, Email


#DataRequired == Making sure the field in
#Equalto == Naking sure the field(s)  are the same (ie. Password and Confirm Password)
#Email == Making sure the field has a proper email given

class UserInfoForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('password', validators = [DataRequired()])
    confirm_pass = PasswordField('confirm password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField()

class PostForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    content = TextAreaField('Content', validators = {DataRequired()})
    submit = SubmitField()