import requests


def get_token():
	response = requests.get('http://127.0.0.1:5001/login')
	return response.text


def make_request(token):
	headers = {'Authorization': token}
	response = requests.get('http://127.0.0.1:5001/profile', headers=headers)
	return response.text


if __name__ == '__main__':
	token = get_token()
	result = make_request(token)
	print(result)
