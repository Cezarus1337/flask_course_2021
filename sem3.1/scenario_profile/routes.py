import os

from flask import Blueprint, request, current_app, render_template

from sql_provider import SQLProvider
from database import DBConnection, work_with_db


profile_app = Blueprint('profile', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@profile_app.route('/', methods=['GET', 'POST'])
def profile_index():
	if request.method == 'GET':
		return render_template('profile-user.html', name='Ivan')
	else:
		user_name = request.form['user_name']
		sql = provider.get('user.sql', user_name=user_name)
		user = work_with_db(current_app.config['db_config'], sql)
		return render_template('profile-result.html', user=user)


@profile_app.route('/section1')
def handle_section_1():
	return 'Section 1'


@profile_app.route('/section2')
def handle_section_2():
	return 'Section 2'
