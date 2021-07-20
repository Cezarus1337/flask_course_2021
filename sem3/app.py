from flask import Flask, render_template

from blueprints.profile import profile_bp
from blueprints.auth import auth_bp

app = Flask(__name__, template_folder='templates', static_folder='static')

app.register_blueprint(profile_bp, url_prefix='/profile')
app.register_blueprint(auth_bp, url_prefix='/auth')


@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5001)
