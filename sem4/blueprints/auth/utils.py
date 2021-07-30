import base64

from functools import wraps
from datetime import datetime

from flask import session, redirect


def is_decoded(login, token):
	decoded_token = base64.b64decode(token).decode('UTF8').split('|')
	if not decoded_token:
		return False
	decoded_login = decoded_token[0]
	decoded_expire = datetime.strptime(decoded_token[1], '%Y-%m-%d %H:%M:%S.%f')
	if decoded_login == login and datetime.now() < decoded_expire:
		return True
	return False


def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		if 'login' in session and 'token' in session:
			login = session['login']
			token = session['token']
			if is_decoded(login, token):
				return f(*args, **kwargs)
		return redirect('/login')
	return wrapper
