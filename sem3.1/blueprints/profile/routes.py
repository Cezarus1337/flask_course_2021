import os

from flask import Blueprint, request
from flask import render_template, current_app

from sql_provider import SQLProvider
from database import DBConnection


profile_bp = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@profile_bp.route('/')
def profile_index():
	return render_template('profile-index.html', name='Ivan')


@profile_bp.route('/find', methods=['GET', 'POST'])
def profile_info():
	if request.method == 'GET':
		return render_template('profile-find-user.html')
	else:
		user_name = request.form['user_name']
		user = None
		with DBConnection(current_app.config['db_config']) as cursor:
			_sql = provider.get('user.sql', user_name=user_name)
			cursor.execute(_sql)
			description = [column[0] for column in cursor.description]
			row = cursor.fetchone()
			if row:
				user = dict(zip(description, row))
		if user is None:
			return 'Not found'
		return """
		<p>Name: {0}</p>
		<p>Login: {1}</p>
		<p>Password: {2}</p>
		""".format(user['name'], user['login'], user['password'])

