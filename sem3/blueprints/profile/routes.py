import os

from flask import Blueprint
from flask import render_template

from sql_provider import SQLProvider


profile_bp = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@profile_bp.route('/')
def profile_index():
	return render_template('profile-index.html')


@profile_bp.route('/<user_id>')
def profile_info(user_id):
	return provider.get('user', user_id=user_id)
