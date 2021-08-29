from functools import wraps

from flask import request
from flask import session, redirect, current_app


class AccessManager:

	@staticmethod
	def login_required(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			group = session.get('group', None)
			if group is not None and group != '':
				return f(*args, **kwargs)
			return redirect('/login')
		return wrapper

	@staticmethod
	def group_required(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			if 'group' in session:
				group = session['group']
				config = current_app.config['ACCESS_CONFIG']
				if group in config:
					handler = request.endpoint.split('.')[0]
					if handler in config[group]['blueprints'] or handler in config[group]['endpoints']:
						return f(*args, **kwargs)
			return redirect('/login')
		return wrapper
