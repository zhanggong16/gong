pre_code = '''
from flask import Blueprint
from flask import request
from flask import render_template

bp = Blueprint('index', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
'''
