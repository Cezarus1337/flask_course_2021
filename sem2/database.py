from pymysql import connect
from pymysql.err import ProgrammingError


class DBConnection:

    def __init__(self, config):
        self.config = config
        self.cursor = None
        self.connection = None

    def __enter__(self):
        try:
            self.connection = connect(**self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except ProgrammingError:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        return True
