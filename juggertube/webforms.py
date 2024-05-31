from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField, DateField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
	email = EmailField("Email", validators=[DataRequired()])
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Submit")


class VideoForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	user_id = IntegerField("ChannelID", validators=[DataRequired()])
	link = StringField("Link", validators=[DataRequired()])
	tournament_id = IntegerField("TournamentID", validators=[DataRequired()])
	team_one_id = IntegerField("TeamOneID", validators=[DataRequired()])
	team_two_id = IntegerField("TeamTwoID", validators=[DataRequired()])
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


class ChannelForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	link = StringField("Link", validators=[DataRequired()])
	submit = SubmitField("Submit")
