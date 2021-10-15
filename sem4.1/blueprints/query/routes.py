from flask import Blueprint, render_template
from access import AccessManager

query_app = Blueprint('query', __name__, template_folder='templates')


@query_app.route('/')
@AccessManager.group_required
def query_index():
	return render_template('query-index.html')
