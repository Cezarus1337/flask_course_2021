from flask import render_template

from . import profile_bp
from . import provider


@profile_bp.route('/')
def profile_index():
	return render_template('profile/index.html')


@profile_bp.route('/<user_id>')
def profile_info(user_id):
	return provider.get('user', user_id=user_id)
