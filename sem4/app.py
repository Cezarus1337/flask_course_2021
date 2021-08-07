import yaml

from flask import Flask, render_template

app = Flask(__name__)

app.config['DB_CONFIG'] = yaml.safe_load(open('configs/db.yaml'))
app.config['ACCESS_CONFIG'] = yaml.safe_load(open('configs/access.yaml'))
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
