from flask import Blueprint

from sql_provider import SQLProvider


auth_bp = Blueprint('auth', __name__, template_folder='templates', static_folder='static')
provider = SQLProvider('/blueprints/auth/sql/')

from . import routes
