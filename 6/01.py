import sqlite3
from sqlite3 import Error


class SqliteDatabase:
    conn = ()

    def __init__(self, db_location=':memory:'):
        self.db_location = db_location

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_location)
        except Error as e:
            print(e)

    def create_tables(self,model):



if __name__ == '__main__':
    db = SqliteDatabase()
    print(db)
