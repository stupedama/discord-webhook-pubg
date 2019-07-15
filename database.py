import sqlite3


class Database:
    def __init(self):
        pass

    def __enter__(self):
        self.conn = sqlite3.connect('.pubg.db', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
        # self.c = self.conn.cursor()
        return self.conn


    def __exit__(self, exc_type, exc_value, tb):
        self.conn.close()
