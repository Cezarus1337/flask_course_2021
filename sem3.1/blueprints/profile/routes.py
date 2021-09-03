import os

from flask import Blueprint, request, current_app, render_template

from sql_provider import SQLProvider
from database import DBConnection, work_with_db


profile_bp = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@profile_bp.route('/')
def profile_index():
	return render_template('profile-index.html', name='Ivan')


@profile_bp.route('/find', methods=['GET', 'POST'])
def profile_search():
	if request.method == 'GET':
		return render_template('profile-search-user.html', name='Ivan')
	else:
		user_name = request.form['user_name']
		_sql = provider.get('user.sql', user_name=user_name)
		user = work_with_db(current_app.config['db_config'], _sql)
		if not user:
			return 'Not found'
		return user[0]
