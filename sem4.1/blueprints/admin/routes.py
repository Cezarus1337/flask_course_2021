from flask import Blueprint, render_template


admin_pb = Blueprint('admin', __name__, template_folder='templates')


@admin_pb.route('/')
def admin_index():
	return render_template('admin-index.html')
