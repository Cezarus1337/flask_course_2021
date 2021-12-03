import os


class Config:
	DB_HOST = os.environ.get('HOST', 'localhost')
	DB_PORT = os.environ.get('PORT', 3306)
	DB_USER = os.environ.get('USER_DB', 'root')
	DB_PASSWORD = os.environ.get('USER_PASSWORD', 'root')
	DB_NAME = os.environ.get('DB_NAME', 'money_db')

	@property
	def db_config(self):
		return {
			'host': self.DB_HOST,
			'port': self.DB_HOST,
			'user': self.DB_USER,
			'password': self.DB_PASSWORD,
			'db': self.DB_NAME
		}
