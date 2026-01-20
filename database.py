
import sqlite3

class Database():

    def __init__(self, conn):

        self.conn = conn
    
    def create_table(self):
        
        cursor = self.conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            title TEXT,
            message TEXT)""")
        
        self.conn.commit()
        
    def add_message(self, title, message):

        self.create_table()
        
        cursor = self.conn.cursor()
        
        cursor.execute("""
        INSERT INTO messages (title, message) VALUES (?, ?)""", (title, message))    
        
        self.conn.commit()

    def print_table(self):

        cursor = self.conn.cursor()
        
        cursor.execute("SELECT * FROM messages")
        
        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        print(colums)
        print(rows)
