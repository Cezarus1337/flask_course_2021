from flask import Flask
from flask.views import MethodView

from middleware import AuthorizationMiddleware

app = Flask(__name__)
app.wsgi_app = AuthorizationMiddleware(app.wsgi_app, auth_urls=['/login'])


class UserAPI(MethodView):

	def get(self, user_id):
		return {
			'id': user_id,
			'name': 'Ivan',
			'login': 'thiendio',
			'email': 'thiendio@example.com'
		}

	def post(self):
		return 'kek'

	def put(self, user_id):
		return str(user_id)

	def delete(self, user_id):
		return str(user_id)


app.add_url_rule('/profile/<int:user_id>', view_func=UserAPI.as_view('user_api'), methods=['GET'])

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5001)
