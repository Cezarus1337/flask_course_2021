from flask import Flask

app = Flask(__name__)


def controller():
	return 'index'


def controller1():
	return 'Item 1'


def controller2():
	return 'Item 2'


def global_conroller(app):
	app.add_url_rule('/', view_func=controller)
	app.add_url_rule('/item1', view_func=controller1)
	app.add_url_rule('/item2', view_func=controller2)
	return app


if __name__ == '__main__':
	app = global_conroller(app)
	app.run(host='127.0.0.1', port=5001)
