import json

from flask import Flask

app = Flask(__name__)

app.config['DB_CONFIG'] = json.load(open('configs/db.json'))
app.config['ACCESS_CONFIG'] = json.load(open('configs/access.json'))
app.config['SECRET_KEY'] = 'super secret key'


from blueprints.auth.routes import auth_pb
from blueprints.admin.routes import admin_pb
from access import AccessManager
from utils import local_routing

app.register_blueprint(auth_pb, url_prefix='/auth')
app.register_blueprint(admin_pb, url_prefix='/admin')


@app.route('/')
@AccessManager.group_required
def index():
	return local_routing(url_key='url', default_page='index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
