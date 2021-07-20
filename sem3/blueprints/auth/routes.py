from flask import render_template, request

from . import auth_bp
from . import provider


@auth_bp.route('/')
def auth_index():
	return render_template('auth/index.html')


@auth_bp.route('/register')
def auth_register():
	return 'Register'


@auth_bp.route('/check', methods=['POST'])
def auth_authenticate():
	login = request.form.get('login')
	password = request.form.get('password')
	return provider.get('login_password', login=login, password=password)
