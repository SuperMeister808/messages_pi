
import sqlite3

class Database():

    def __init__(self):

        self.conn = None

        self.cursor = None
    
    def connect_to_database(self):

        self.conn = sqlite3.connect("messages.db")

        self.cursor = self.conn.cursor()

    def create_table(self):

        self.connect_to_database()
        
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    titel TEXT,
    message TEXT)""")
        self.conn.commit()

        self.close_connection()
        
    def add_message(self, titel, message):

        self.connect_to_database()

        self.cursor.execute(f"""
INSERT INTO messages (titel, message) VALUES (?, ?)""", (titel, message))    
        self.conn.commit()

        self.close_connection()

    def print_table(self):

        self.connect_to_database()
        
        self.cursor.execute("SELECT * FROM messages")
        print(self.cursor.fetchall())

        self.close_connection()

    def close_connection(self):

        self.conn.close()