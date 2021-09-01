import os

from flask import Blueprint
from flask import session
from flask import render_template, request, current_app, redirect

from database.connection import DBConnection, make_request
from database.sql_provider import SQLProvider
from utils import local_routing


auth_pb = Blueprint('auth', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@auth_pb.route('/login', methods=['GET', 'POST'])
def login_page():
	if request.method == 'GET':
		return local_routing(url_key='url', default_page='login.html')
	else:
		login = request.form['login']
		password = request.form['password']
		sql = provider.get('user.sql', login=login, password=password)
		user = make_request(current_app.config['DB_CONFIG'], sql)
		if not user:
			return render_template('login.html', message='Invalid login or password')
		user = user[0]
		group_name = user['group_name']
		session['group'] = group_name
		session.permanent = True
		return redirect('/')


@auth_pb.route('/logout')
def logout():
	session.clear()
	return redirect('/')
