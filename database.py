
import sqlite3

class Database():

    def create_table(self, conn):
        
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages(
            titel TEXT,
            message TEXT)""")
        
        conn.commit()
        
    def add_message(self, conn, titel, message):

        self.create_table(conn)
        
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO messages (titel, message) VALUES (?, ?)""", (titel, message))    
        
        conn.commit()
    
    def print_table(self):

        with sqlite3.connect("messages.db") as conn:
        
            cursor = conn.cursor()
        
            cursor.execute("SELECT * FROM messages")
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            print(colums)
            print(rows)



