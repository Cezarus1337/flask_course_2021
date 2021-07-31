import os
import base64

from datetime import datetime
from datetime import timedelta

from flask import Blueprint
from flask import session
from flask import render_template, request, current_app, redirect

from database.connection import DBConnection
from database.sql_provider import SQLProvider


auth_pb = Blueprint('auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@auth_pb.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		token = None
		login = request.form['login']
		password = request.form['password']
		with DBConnection(current_app.config['db_config']) as cursor:
			sql = provider.get('user.sql', login=login, password=password)
			cursor.execute(sql)
			user = cursor.fetchone()
			if user:
				token_expire = f'{datetime.now() + timedelta(seconds=60)}'
				token = base64.b64encode(f'{login}|{token_expire}'.encode('UTF8'))
				session['login'] = login
				session['token'] = token
				session.permanent = True
				return redirect('/')
		if token is None:
			return render_template('login.html', message='Invalid login or password')


@auth_pb.route('/logout')
def logout():
	if 'login' in session and 'token' in session:
		session.pop('login')
		session.pop('token')
	return redirect('/login')
