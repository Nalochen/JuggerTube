from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, DateField, EmailField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, EqualTo, Optional

from juggertube.game_system_enum import GameSystem
from juggertube.video_type_enum import VideoType


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password",
                             validators=[DataRequired(), EqualTo('password2', message='Passwords must match!')])
    password2 = PasswordField("Confirm 'Password", validators=[DataRequired()])
    team = SelectField("Team", validators=[Optional()])
    submit = SubmitField("Submit")


class VideoForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    channel = SelectField("Channel", validators=[DataRequired()])
    link = StringField("Link", validators=[DataRequired()])
    category = SelectField("Category",
                           choices=[(choice.name, choice.value) for choice in VideoType],
                           validators=[DataRequired()])
    tournament = SelectField("Tournament", validators=[Optional()])
    team_one = SelectField("TeamOne", validators=[Optional()])
    team_two = SelectField("TeamTwo", validators=[Optional()])
    upload_date = DateField("Date", validators=[DataRequired()])
    date_of_recording = DateField("Date", validators=[Optional()])
    game_system = SelectField("Game System",
                              choices=[('', 'Select an Option')] +
                                      [(choice.name, choice.value) for choice in GameSystem],
                              validators=[Optional()]
                              )
    weapon_type = StringField("Weapon Type", validators=[Optional()])
    topic = StringField("Topic", validators=[Optional()])
    guests = StringField("Guests", validators=[Optional()])
    comments = TextAreaField("Comments", validators=[Optional()])
    submit = SubmitField("Submit")


class TournamentForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    jtr_link = StringField("JTRLink", validators=[Optional()])
    tugeny_link = StringField("Tugeny Link", validators=[Optional()])
    submit = SubmitField("Submit")


class TeamForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    country = StringField("Country", validators=[DataRequired()])
    submit = SubmitField("Submit")


class ChannelForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    link = StringField("Link", validators=[DataRequired()])
    owner = SelectField("Owner", validators=[Optional()])
    submit = SubmitField("Submit")
