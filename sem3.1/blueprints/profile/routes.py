import os

from flask import Blueprint, request, current_app

from sql_provider import SQLProvider
from database import DBConnection, make_request
from utils import local_routing


profile_bp = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@profile_bp.route('/')
def profile_index():
	return local_routing(url_key='url', default_page='profile-index.html')


@profile_bp.route('/find', methods=['GET', 'POST'])
def profile_info():
	if request.method == 'GET':
		return local_routing(url_key='url', default_page='profile-find-user.html', name='Ivan')
	else:
		user_name = request.form['user_name']
		_sql = provider.get('user.sql', user_name=user_name)
		user = make_request(current_app.config['db_config'], _sql)
		if not user:
			return 'Not found'
		return user[0]
