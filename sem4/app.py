from flask import Flask, render_template

app = Flask(__name__)

db_config = {
	'host': '127.0.0.1',
	'port': 3306,
	'user': 'root',
	'password': 'root',
}

app.secret_key = 'super secret key'
app.config['db_config'] = db_config


from blueprints.auth.routes import auth_pb
from blueprints.auth.utils import login_required

app.register_blueprint(auth_pb, url_prefix='/')


@app.route('/order')
@login_required
def order_page():
	return 'Order page'


@app.route('/user')
@login_required
def profile_page():
	return 'Profile page'


@app.route('/admin')
@login_required
def admin_page():
	return 'Admin page'


@app.route('/')
@login_required
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
