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
	team = SelectField("Team")
	submit = SubmitField("Submit")


class VideoForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	channel = SelectField("Tournament", validators=[DataRequired()])
	link = StringField("Link", validators=[DataRequired()])
	category = SelectField("Category")
	tournament = SelectField("Tournament")
	team_one = SelectField("TeamOne")
	team_two = SelectField("TeamTwo")
	upload_date = DateField("Date", validators=[DataRequired()])
	date_of_recording = DateField("Date")
	game_system = SelectField("Game System")
	weapon_type = StringField("Weapon Type")
	topic = StringField("Topic")
	guests = StringField("Guests")
	comments = TextAreaField("Comments")
	submit = SubmitField("Submit")


class TournamentForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	city = StringField("City", validators=[DataRequired()])
	jtr_link = StringField("JTRLink", validators=[DataRequired()])
	tugeny_link = StringField("Tugeny Link")
	submit = SubmitField("Submit")


class TeamForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	city = StringField("City", validators=[DataRequired()])
	country = StringField("Country", validators=[DataRequired()])
	submit = SubmitField("Submit")


class ChannelForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	link = StringField("Link", validators=[DataRequired()])
	owner = SelectField("Owner", validators=[DataRequired()])
	submit = SubmitField("Submit")

