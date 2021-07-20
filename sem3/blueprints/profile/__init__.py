from flask import Blueprint

from sql_provider import SQLProvider


profile_bp = Blueprint('profile', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('/blueprints/profile/sql/')

from . import routes
