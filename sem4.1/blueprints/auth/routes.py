import os

from flask import (
	Blueprint, session, render_template,
	request, current_app, redirect)

from database.connection import DBConnection, work_with_db
from database.sql_provider import SQLProvider


auth_app = Blueprint('auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@auth_app.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		login = request.form['login']
		password = request.form['password']
		sql = provider.get('user.sql', login=login, password=password)
		user = work_with_db(current_app.config['DB_CONFIG'], sql)
		if not user:
			return render_template('login.html', message='Invalid login or password')
		user = user[0]
		group_name = user['group_name']
		session['group'] = group_name
		session.permanent = True
		return redirect('/')


@auth_app.route('/logout')
def logout():
	session.clear()
	return redirect('/')
