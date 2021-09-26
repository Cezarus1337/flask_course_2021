from pymysql import connect
from pymysql.err import OperationalError


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
        except OperationalError:
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None and self.cursor is not None:
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        if exc_val is not None:
            print(exc_type)
            print(exc_val.args[0])
        return True


def work_with_db(db_config, sql):
    items = []
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        for item in cursor.fetchall():
            items.append(dict(zip(schema, item)))
    return items
