from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

db_config = {
	'host': '127.0.0.1',
	'port': 3306,
	'user': 'root',
	'password': 'root',
	'database': 'joom'
}

app.config['db_config'] = db_config

from blueprints.profile.routes import profile_bp


def index():
	return render_template('index.html')


def goodbye():
	return 'Goodbye'


app.add_url_rule('/', view_func=index, methods=['GET'])
app.add_url_rule('/exit', view_func=goodbye, methods=['GET'])
app.register_blueprint(profile_bp, url_prefix='/profile')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
