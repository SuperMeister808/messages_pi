
import sqlite3

class Database():

    def create_table(self):
        
        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        
        cursor.execute("""
CREATE TABLE IF NOT EXISTS messages(
    titel TEXT,
    message TEXT)""")
        conn.commit()

        conn.close()
        
    def add_message(self, titel, message):

        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()

        cursor.execute("""
INSERT INTO messages (titel, message) VALUES (?, ?)""", (titel, message))    
        conn.commit()

        conn.close()

    def print_table(self):

        conn = sqlite3.connect("messages.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM messages")
        colums = [desc[0] for desc in self.cursor.description]
        rows = cursor.fetchall()

        print(colums)
        print(rows)

        conn.close()

