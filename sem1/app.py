import random
from datetime import datetime

from flask import Flask
from flask import render_template  # draw html code

app = Flask(__name__)


# simple handler
@app.route('/')
def index():
	return 'Hello World'


# static html page
@app.route('/static')
def static_index_page():
	return render_template('static_index.html')


# dynamic html page
@app.route('/dynamic')
def dynamic_index_page():
	urls = [
		'https://img.championat.com/s/735x490/news/big/u/x/sbornaya-rossii-i-olimpiada_1624534585660408328.jpg',
		'https://cdnimg.rg.ru/i/gallery/9ff08936/18_4c1f95d6.jpg',
		'https://cdnimg.rg.ru/i/gallery/9ff08936/9_cdfcd9d3.jpg'
	]

	title = 'Турнир по баскетболу ' + str(datetime.now().year)
	url = urls[random.randint(0, len(urls) - 1)]  # выбираем наугад картинку для отображения
	title_small = 'Список лидеров'
	items = [
		'ЦСКА',
		'Динамо',
		'Спартак'
	]
	random.shuffle(items)  # перемешиваем рейтинг команд
	return render_template('dynamic_index.html', title=title, image_url=url, title_small=title_small, list_items=items)


# inherit html base
@app.route('/bitcoin')
def bitcoin_page():
	return render_template('bitcoin.html')


if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000)  # run application
