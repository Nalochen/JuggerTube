from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField, DateField, EmailField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
	email = EmailField("Email", validators=[DataRequired()])
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired(), EqualTo('password2', message='Passwords must match!')])
	password2 = PasswordField("Confirm 'Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


class VideoForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	link = StringField("Link", validators=[DataRequired()])
	tournament = SelectField("Tournament", validators=[DataRequired()])
	team_one = SelectField("TeamOne", validators=[DataRequired()])
	team_two = SelectField("TeamTwo", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	comments = TextAreaField("Comments")
	submit = SubmitField("Submit")


class TournamentForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	date_beginning = DateField("DateBeginning", validators=[DataRequired()])
	date_ending = DateField("DateEnding", validators=[DataRequired()])
	city = StringField("City", validators=[DataRequired()])
	jtr_link = StringField("JTRLink", validators=[DataRequired()])
	submit = SubmitField("Submit")


class TeamForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	city = StringField("City", validators=[DataRequired()])
	country = StringField("Country", validators=[DataRequired()])
	submit = SubmitField("Submit")

