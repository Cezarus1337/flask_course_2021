from flask import Flask

from access import AccessManager
from utils import local_routing

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

app.register_blueprint(profile_bp, url_prefix='/profile')


@app.route('/')
@AccessManager.group_reguired
def index():
	return local_routing(url_key='url', default_page='index.html')


@app.route('/exit')
def goodbye():
	return 'Goodbye'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
