import json
from flask import Flask, request

from config import Config
from database.utils import make_db_request
from database.sql_provider import SQLProvider
from middleware.auth import AuthorizationMiddle

app = Flask(__name__)
app.config.from_object(Config())
app.wsgi_app = AuthorizationMiddle(app.wsgi_app)

provider = SQLProvider('sql/')


@app.route('/get-money')
def get_money():
	user_id = request.headers.get('auth_middleware_user')
	sql = provider.get('get_money.sql', user_id=user_id)
	result = make_db_request(app.config, sql, method='select')
	return json.dumps(result)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
