import base64

from datetime import datetime, timedelta
from werkzeug.wrappers import Request, Response


class AuthorizationMiddleware(object):

	def __init__(self, app, auth_urls):
		self.app = app
		self.auth_urls = auth_urls
		self.token_storage = {}

	def _generate_token(self, username, password):
		expire = datetime.now() + timedelta(seconds=60)
		new_token = base64.b64encode(f'authentication|{username}|{password}|{expire}'.encode('UTF-8')).decode()
		self.token_storage[(username, password)] = new_token
		return new_token

	@staticmethod
	def parse_token(encrypt_token):
		return base64.b64decode(encrypt_token).decode().split('|')

	def _valid_token(self, parsed_token):
		if len(parsed_token) == 4:
			if parsed_token[0] == 'authentication' and \
				(parsed_token[1], parsed_token[2]) in self.token_storage and \
				datetime.strptime(parsed_token[3], '%Y-%m-%d %H:%M:%S.%f') > datetime.now():
				return True
		return False

	def __call__(self, environ, start_response):
		request = Request(environ)
		if request.path in self.auth_urls:
			request_data = request.get_json()
			username = request_data['username']
			password = request_data['password']
			return Response(self._generate_token(username, password))(environ, start_response)
		else:
			token = request.headers.get('Authorization', '')
			parsed_token = self.parse_token(token)
			if token != '' and self._valid_token(parsed_token):
				return self.app(environ, start_response)
			return Response('Bad response', status=400)(environ, start_response)
