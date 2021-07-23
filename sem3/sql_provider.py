import os

from string import Template


class SQLProvider:

	def __init__(self, file_path: str) -> None:
		self._file_path = file_path
		self._scripts = {}

		for file in os.listdir(file_path):
			key = file.replace('.sql', '')
			self._scripts[key] = Template(open(f'{file_path}/{file}').read())

	def get(self, name, **kwargs) -> str:
		return self._scripts.get(name, '').substitute(**kwargs)
