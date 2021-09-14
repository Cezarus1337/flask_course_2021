from flask import Flask
from flask import request, render_template, redirect

from database import DBConnection


db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root'
}

app = Flask(__name__)


@app.route('/db-version')
def get_db_version():
    version = 'Unknown'
    with DBConnection(db_config) as cursor:
        if cursor is None:
            raise ValueError('No connection')
        cursor.execute('select version()')
        version = cursor.fetchone()[0]
    return f'DB Version: {version}'


@app.route('/')
@app.route('/<param>')
def get_param(param=None):
    if param is not None:
        return f'Params: {param}'
    else:
        return 'No params'


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


@app.route('/args')
def page_with_args():
    target = request.args.get('target', None)
    if target is not None:
        target_urls = {
            'source1': '/',  # start page
            'source2': '/db-version'  # stay here
        }
        next_url = target_urls.get(target, '/')
        return redirect(next_url)
    return render_template('start-page.html')


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


# @app.route('/upload-file', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'GET':
#         return render_template('input_file.html')
#     elif request.method == 'POST':
#         file = request.files.get('file')
#         if file.filename:
#             file.save(os.path.join('static/images/', file.filename))
#             return render_template('image_page.html', url=os.path.join('/static/images/', file.filename))
#         else:
#             return render_template('input_file.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
