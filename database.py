
import sqlite3

class Database():

    def __init__(self):

        self.conn = None
    
    def connect_to_database(self):

        self.conn = sqlite3.connect("messages.db")

        cursor = self.conn.cursor()

        cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    titel TEXT,
    message TEXT)""")
        
        self.conn.commit()

        self.conn.close()
        
    def add_message(self, titel, message):

        self.conn = sqlite3.connect("messages.db")

        cursor = self.conn.cursor()

        cursor.execute(f"""
INSERT INTO messages (titel, message) VALUES (?, ?)""", (titel, message))
        
        self.conn.commit()

        self.conn.close()