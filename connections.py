
from dataclasses import dataclass
import sqlite3

class CollectConnections():

    connections = []

    def __init__(self, conn):

        self.conn = conn
    
    @dataclass
    class Connection():

        conn: sqlite3.Connection

    def collect_connection(self):

        c = self.Connection(self.conn)

        self.append_connection(c)

    @classmethod
    def append_connection(cls, c):
        
        cls.connections.append(c)

    @classmethod
    def clear_connections(cls):

        cls.connections.clear()

    