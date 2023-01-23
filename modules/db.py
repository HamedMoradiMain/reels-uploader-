import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, post text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, user text, password text, platform text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS description (id INTEGER PRIMARY KEY, description text)")
        self.conn.commit()
    def fetch(self,tablename):
        self.cur.execute(f"SELECT * FROM {tablename}")
        rows = self.cur.fetchall()
        return rows
    def remove(self, id,tablename):
        self.cur.execute(f"DELETE FROM {tablename} WHERE id=?", (id,))
        self.conn.commit()
    def insert_to_posts(self, post):
        self.cur.execute("INSERT INTO posts VALUES (NULL, ?)",(post,))
        self.conn.commit()
    def update_posts(self, id, post):
        self.cur.execute("UPDATE parts SET post = ?,WHERE id = ?",(post,id))
        self.conn.commit()
    def insert_to_accounts(self, user,password,platform):
        self.cur.execute("INSERT INTO accounts VALUES (NULL,?,?,?)",(user,password,platform))
        self.conn.commit()
    def update_accounts(self, id, user,password,platform):
        self.cur.execute("UPDATE parts SET user = ?,WHERE password=?,WHERE id = ?",(user,password,platform,id,))
        self.conn.commit()
    def insert_to_description(self,description):
        self.cur.execute("INSERT INTO description VALUES (NULL,?)",(description))
        self.conn.commit()
    def update_description(self,id,description):
        self.cur.execute("UPDATE description SET description = ?,WHERE id = ?",(description,id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()