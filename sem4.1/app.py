import json

from flask import Flask, render_template

app = Flask(__name__)

app.config['DB_CONFIG'] = json.load(open('configs/db.json'))
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))
app.config['SECRET_KEY'] = 'super secret key'


from blueprints.auth.routes import auth_pb
from access import AccessManager


# @app.route('/order/')
@AccessManager.login_required
def order_page():
	return 'Order page'


# @app.route('/user')
@AccessManager.login_required
def profile_page():
	return 'Profile page'


# @app.route('/admin')
@AccessManager.group_required
def admin_page():
	return 'Admin page'


# @app.route('/')
def index():
	return render_template('index.html')


app.add_url_rule('/', view_func=index)
app.add_url_rule('/admin', view_func=admin_page)
app.add_url_rule('/user', view_func=profile_page)
app.add_url_rule('/order/', view_func=order_page)
app.register_blueprint(auth_pb, url_prefix='/')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
