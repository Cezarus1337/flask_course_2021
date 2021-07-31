from typing import Optional

from pymysql import connect
from pymysql import Connection
from pymysql.cursors import Cursor
from pymysql.err import OperationalError


class DBConnection:

    def __init__(self, config: dict) -> None:
        self.config: dict = config
        self.cursor: Optional[Cursor] = None
        self.connection: Optional[Connection] = None

    def __enter__(self) -> Optional[Cursor]:
        try:
            self.connection = connect(**self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except OperationalError:
            return None

    def __exit__(self, exc_type: Optional, exc_val: Optional, exc_tb: Optional) -> bool:
        if self.connection is not None and self.cursor is not None:
            self.connection.commit()
            self.connection.close()
            self.cursor.close()
        if exc_val is not None:
            print(exc_type)
            print(exc_val.args[0])
            print(exc_val)
            print(exc_tb)
        return True
