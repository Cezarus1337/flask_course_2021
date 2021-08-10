import os

from flask import Flask, request
from flask.views import MethodView

from database import DBConnection, SQLProvider
from middleware import AuthorizationMiddleware

app = Flask(__name__)
app.config['DB_CONFIG'] = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': 'root'}
app.wsgi_app = AuthorizationMiddleware(app.wsgi_app, auth_urls=['/login'])

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


class UserAPI(MethodView):

	def get(self, username):
		user = None
		with DBConnection(app.config['DB_CONFIG']) as cursor:
			if cursor is None:
				raise ValueError('Cursor is None')
			sql = provider.get('get_user.sql', username=username)
			cursor.execute(sql)
			user = cursor.fetchone()
			schema = [column[0] for column in cursor.description]
		if user:
			user = dict(zip(schema, user))
			return user
		else:
			return {}

	def post(self):
		body = request.get_json()
		with DBConnection(app.config['DB_CONFIG']) as cursor:
			if cursor is None:
				raise ValueError('Cursor is None')
			get_sql = provider.get('get_user.sql', username=body['name'])
			cursor.execute(get_sql)
			if cursor.fetchone():
				return {'Message': 'User with this name already exists'}
			create_sql = provider.get('create_user.sql', **body)
			cursor.execute(create_sql)
		return str(body)


user_api_view = UserAPI.as_view('user_api')

app.add_url_rule('/profile/<username>', view_func=user_api_view, methods=['GET'])
app.add_url_rule('/profile', view_func=user_api_view, methods=['POST'])

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001)
