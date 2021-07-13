import os

from flask import Flask
from flask import request, render_template, redirect


app = Flask(__name__)


@app.route('/')
@app.route('/<param>')
def index(param=None):
    if param is not None:
        return f'Params: {param}'
    else:
        return 'Hello World'


@app.route('/users/<int:user_id>')
def user_page(user_id: int):

    users = [
        {'id': 1, 'name': 'Nick', 'email': 'nick@google.com'},
        {'id': 2, 'name': 'Mike', 'email': 'mike@google.com'},
        {'id': 3, 'name': 'John', 'email': 'john@google.com'},
    ]

    user = None
    for _user in users:
        if _user['id'] == user_id:
            user = _user
            break

    if user is None:
        return 'Not found'
    return f"User profile:\nname: {user['name']}\nemail: {user['email']}"


@app.route('/sum')  # Доп. задание - калькулятор на args
def page_with_args():
    x = float(request.args.get('x', 0))
    y = float(request.args.get('y', 0))
    return f'Result: {x + y}'


@app.route('/user-form')
def user_input_page_1():
    return render_template('input_form_redirect.html')


@app.route('/user-form-next', methods=['POST'])
def user_input_page_2():
    login = request.form.get('login', '')
    password = request.form.get('password', '')
    if login and password:
        return {'login': login, 'password': password}
    else:
        return 'Wrong input'


@app.route('/user-form-all', methods=['GET', 'POST'])  # Доп. - получить данные пользователя и вернуть страничку с его профилем
def user_input():
    if request.method == 'GET':
        return render_template('input_form_self.html')
    elif request.method == 'POST':
        login = request.form.get('login', None)
        password = request.form.get('password', None)
        if login and password:
            return redirect('/')
        else:
            return 'Wrong input'


@app.route('/upload-file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('input_file.html')
    elif request.method == 'POST':
        file = request.files.get('file')
        if file.filename:
            file.save(os.path.join('static/images/', file.filename))
            return render_template('image_page.html', url=os.path.join('/static/images/', file.filename))
        else:
            return render_template('input_file.html')


# curl -X POST http://localhost:5000/api/user -d "{\"name\": \"Ivan\"}" -H "Content-Type: application/json"
@app.route('/api/user', methods=['POST'])
def api_user_create():
    return ''.join([request.get_data(as_text=True), str(request.get_json())])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
