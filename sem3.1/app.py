from flask import Flask, render_template

app = Flask(__name__)

db_config = {
	'host': '127.0.0.1',
	'port': 3306,
	'user': 'root',
	'password': 'root',
	'database': 'joom'
}

app.config['db_config'] = db_config

from scenario_profile.routes import profile_app

app.register_blueprint(profile_app, url_prefix='/profile')


@app.route('/')
def index():
	return render_template('menu.html')


@app.route('/exit')
def goodbye():
	return 'Goodbye'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
