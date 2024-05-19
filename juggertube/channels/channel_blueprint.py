from flask import Blueprint, request, url_for, redirect, render_template

from models import Channel, db

channel_blueprint = Blueprint('channels', __name__, template_folder='templates')


@channel_blueprint.route('/add', methods=['GET', 'POST'])
def add_channel():
    if request.method == 'POST':
        name = request.form['name']
        link = request.form['link']
        new_channel = Channel(name=name, link=link)
        db.session.add(new_channel)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_channel.html')
