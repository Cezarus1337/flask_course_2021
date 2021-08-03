from functools import wraps

from flask import session, redirect, render_template


def login_required(f):
	@wraps(f)
	def wrapper(*args, **kwargs):
		group = session.get('group', None)
		if group is not None and group != '':
			return f(*args, **kwargs)
		return redirect('/login')
	return wrapper


def role_required(role):
	def wrapper_args(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			if session.get('group', None) == role:
				return f(*args, **kwargs)
			else:
				return render_template('permission.html')
		return wrapper
	return wrapper_args
