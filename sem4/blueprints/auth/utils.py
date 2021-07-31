import base64

from functools import wraps
from datetime import datetime

from flask import session, redirect


def parse_token(token):
	try:
		decoded = base64.b64decode(token).decode('UTF8').split('/')
		token_dict = dict(zip(['group_login', 'group_password', 'expire'], decoded))
		return token_dict
	except Exception as e:
		print('Could not parse user token')
		print(e.args)
	return None


def is_valid_token(token_info):
	try:
		for value in token_info.values():
			if value is None or value == '':
				return False
		expire = datetime.strptime(token_info['expire'], '%Y-%m-%d %H:%M:%S.%f')
		if datetime.now() > expire:
			return False
	except Exception as e:
		print(e)
		return False
	return True


def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		token_info = parse_token(session.get('token', None))
		if is_valid_token(token_info):
			return f(*args, **kwargs)
		return redirect('/login')
	return wrapper
