from typing import Union

from database.connection import DBConnection


def select_from_db(config: dict, sql: str) -> list:
    items = []
    with DBConnection(config) as cursor:
        if cursor is None:
            raise ValueError('Is None')
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        for item in cursor.fetchall():
            items.append(dict(zip(schema, item)))
    return items


def insert_into_db(config: dict, sql: str) -> int:
    result = 0
    with DBConnection(config) as cursor:
        if cursor is None:
            raise ValueError('Is None')
        result = cursor.execute(sql)
    return result


def make_db_request(config: dict, sql: str, method: str) -> Union[int, list]:
    if method not in ['select', 'insert']:
        raise ValueError('invalid db method')
    db_config = {
        'host': config['DB_HOST'],
        'port': config['DB_PORT'],
        'user': config['DB_USER'],
        'password': config['DB_PASSWORD'],
        'db': config['DB_NAME']
    }
    if method == 'select':
        return select_from_db(db_config, sql)
    else:
        return insert_into_db(db_config, sql)
