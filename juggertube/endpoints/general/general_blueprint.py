from flask import Blueprint, render_template, flash, redirect, url_for

general_blueprint = Blueprint('general', __name__, template_folder='templates')


@general_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')