from flask import Blueprint, render_template
from access import AccessManager


admin_app = Blueprint('admin', __name__, template_folder='templates')


@admin_app.route('/')
@AccessManager.group_required
def admin_index():
	return render_template('admin-index.html')
