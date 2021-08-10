import json
import requests


def get_token():
	headers = {'Content-Type': 'application/json'}
	data = json.dumps({'username': 'thiendio', 'password': 'thiendio'})
	response = requests.post('http://127.0.0.1:5001/login', headers=headers, data=data)
	return response.text


def make_get_request(token):
	headers = {'Authorization': token}
	response = requests.get('http://127.0.0.1:5001/profile/ivan', headers=headers)
	return response.text


def make_post_request(token):
	headers = {'Authorization': token, 'Content-Type': 'application/json'}
	data = json.dumps({'name': 'new_user', 'login': 'test_login', 'password': 'test_password'})
	response = requests.post('http://127.0.0.1:5001/profile', headers=headers, data=data)
	return response.text


if __name__ == '__main__':
	token = get_token()
	result = make_get_request(token)
	print(result)
	result = make_post_request(token)
	print(result)
