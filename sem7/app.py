import os
import json

from flask import Flask, render_template

from database import SQLProvider, DBConnection

app = Flask(__name__)

app.config['DB_CONFIG'] = json.loads(open('configs/db.json', 'r').read())
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))


@app.route('/')
def index():
	return 'Hello world'


@app.route('/items')
def all_items():
	result = []
	sql = provider.get('simple.sql')
	with DBConnection(app.config['DB_CONFIG']) as cursor:
		if cursor is None:
			raise ValueError('Cursor is None')
		cursor.execute(sql)
		schema = [column[0] for column in cursor.description]
		for raw in cursor.fetchall():
			item = dict(zip(schema, raw))
			for column in schema:
				item[column] = str(item[column])
			result.append(item)
	return render_template('items.html', items=result)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
