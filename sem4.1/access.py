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
			return redirect('/auth/login')
		return wrapper

	@staticmethod
	def group_required(f):
		@wraps(f)
		def wrapper(*args, **kwargs):
			config = current_app.config['ACCESS_CONFIG']
			if request.args.get('url', '/') in config['public_urls']:
				return f(*args, **kwargs)
			elif 'group' in session:
				group = session['group']
				if group in config:
					path = request.args.get('url', '/')
					if path in config[group]:
						return f(*args, **kwargs)
			return redirect('/auth/login')
		return wrapper
