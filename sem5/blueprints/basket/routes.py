import os

from flask import Blueprint
from flask import session
from flask import render_template, current_app, request, redirect

from database.connection import DBConnection, make_request
from database.sql_provider import SQLProvider
from utils import login_required
from .utils import add_user_basket, clear_user_basket, remove_item_by_id


basket_pb = Blueprint('basket', __name__, template_folder='templates')
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@basket_pb.route('/', methods=['GET', 'POST'])
@login_required
def list_orders():
	if request.method == 'GET':
		current_basket = session.get('basket', [])
		items = make_request(current_app.config['DB_CONFIG'], provider.get('order_list.sql'))
		return render_template('basket_order_list.html', items=items, basket=current_basket)
	else:
		action = request.form['action']
		item_id = request.form['item_id']
		if action == 'Add':
			sql = provider.get('order_item.sql', item_id=item_id)
			item = make_request(current_app.config['DB_CONFIG'], sql)
			if item:
				item = item[0]
			else:
				remove_item_by_id(item_id)
				return render_template('basket_item_absent.html')
			add_user_basket(item)
		return redirect('/order')


@basket_pb.route('/clear')
@login_required
def clear_basket():
	clear_user_basket()
	return redirect('/order')
