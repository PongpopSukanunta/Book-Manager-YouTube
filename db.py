import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, book text, author text)")
        self.conn.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    
    def insert(self, book, author):
        self.cur.execute("INSERT INTO books VALUES (NULL,?, ?)", (book, author))
        self.conn.commit()

    
    def remove(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.conn.commit()


    def update(self, id, book, author):
        self.cur.execute("UPDATE books SET book = ?, author = ? WHERE id = ?", (book, author, id))
        self.conn.commit()


    def __del__(self):
        self.conn.close()


# db = Database('Bookshelf.db')
# db.insert("mindset", "Dr. Carol")
