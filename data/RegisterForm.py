from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length


class RegisterForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    password_again = StringField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    age = StringField('Возраст', validators=[DataRequired()])
    description = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
    category_prog = BooleanField('')
    category_des = BooleanField('')
    category_av = BooleanField('')
    category_mrk = BooleanField('')
    category_tw = BooleanField('')
    worker = BooleanField('')

    submit = SubmitField('Продолжить')