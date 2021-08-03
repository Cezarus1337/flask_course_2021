from flask import Flask, render_template

app = Flask(__name__)

db_config = {
	'host': '127.0.0.1',
	'port': 3306,
	'user': 'root',
	'password': 'root',
}

app.config['DB_CONFIG'] = db_config
app.config['SECRET_KEY'] = 'super secret key'


from blueprints.auth.routes import auth_pb
from blueprints.basket.routes import basket_pb
from utils import login_required, role_required

app.register_blueprint(auth_pb, url_prefix='/')
app.register_blueprint(basket_pb, url_prefix='/order')


@app.route('/user')
@login_required
def profile_page():
	return 'Profile page'


@app.route('/admin')
@role_required('admin')
def admin_page():
	return 'Admin page'


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
