import base64

from datetime import datetime, timedelta
from werkzeug.wrappers import Request, Response


class AuthorizationMiddleware(object):

	def __init__(self, app, auth_urls, backend):
		self.app = app
		self.auth_urls = auth_urls
		self.backend = backend

	@staticmethod
	def _generate_token():
		expire = datetime.now() + timedelta(seconds=60)
		return base64.b64encode(f'authentication|{expire}'.encode('UTF-8')).decode()

	@staticmethod
	def _valid_token(encrypt_token):
		token = base64.b64decode(encrypt_token).decode().split('|')
		if len(token) == 2:
			if token[0] == 'authentication' and datetime.strptime(token[1], '%Y-%m-%d %H:%M:%S.%f') > datetime.now():
				return True
		return False

	def __call__(self, environ, start_response):
		request = Request(environ)
		if request.path in self.auth_urls:
			return Response(self._generate_token())(environ, start_response)
		else:
			token = request.headers.get('Authorization', '')
			if token != '' and self._valid_token(token):
				return self.app(environ, start_response)
			return Response('Bad response', status=400)(environ, start_response)
