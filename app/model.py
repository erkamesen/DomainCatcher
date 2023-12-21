import sqlite3


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.commit()
            self.connection.close()

    def add(self, table_name, data: dict):
        # {'column1': 'value1', 'column2': 42}
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" if isinstance(
            value, str) else str(value) for value in data.values()])

        self.cursor.execute(
            f"INSERT INTO {table_name} ({columns}) VALUES ({values})")

    def get(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"

        self.cursor.execute(query)
        return self.cursor.fetchall()

    def create_table(self, table_name: str, columns):
        # columns = ['column1', 'column2']
        # &
        # columns = {'column1': 'TEXT', 'column2': 'INTEGER'}
        if isinstance(columns, list):  # if type(columns) == list:
            columns_str = ', '.join(columns)
        elif isinstance(columns, dict):  # if type(columns) == dict:
            columns_str = ', '.join(
                [f'{name} {data_type}' for name, data_type in columns.items()])
        else:
            raise ValueError(
                "Columns should be provided as a list or a dictionary.")

        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})")
