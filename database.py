
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

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO messages (titel, message) VALUES (?, ?)""", (titel, message))    
        
        conn.commit()

    def write_on_database(self, titel, message):

        with sqlite3.connect("messages.db") as conn:

            self.create_table(conn)
            self.add_message(conn, titel, message)
    
    def print_table(self):

        with sqlite3.connect("messages.db") as conn:
        
            cursor = conn.cursor()
        
            cursor.execute("SELECT * FROM messages")
            colums = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()

            print(colums)
            print(rows)



