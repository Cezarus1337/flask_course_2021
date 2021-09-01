from flask import Blueprint

from utils import local_routing


admin_pb = Blueprint('admin', __name__, template_folder='templates')


@admin_pb.route('/')
def admin_page():
	return local_routing(url_key='url', default_page='admin-index.html')
