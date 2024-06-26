from flask import Blueprint, render_template

general_blueprint = Blueprint('general', __name__, template_folder='templates')


@general_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@general_blueprint.route('/api/docs', methods=['GET'])
def get_docs():
    return render_template('swaggerui.html')
