import yaml

from flask import Flask, render_template

app = Flask(__name__)

with open('configs/db.yaml') as f:
	db_config = yaml.safe_load(f)

with open('configs/access.yaml') as f:
	access_config = yaml.safe_load(f)

app.config['DB_CONFIG'] = db_config
app.config['ACCESS_CONFIG'] = access_config
app.config['SECRET_KEY'] = 'super secret key'


from blueprints.auth.routes import auth_pb
from utils import AccessManager

app.register_blueprint(auth_pb, url_prefix='/')


@app.route('/order/')
@AccessManager.login_required
def order_page():
	return 'Order page'


@app.route('/user')
@AccessManager.login_required
def profile_page():
	return 'Profile page'


@app.route('/admin')
@AccessManager.group_required
def admin_page():
	return 'Admin page'


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
