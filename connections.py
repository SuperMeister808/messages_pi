
from dataclasses import dataclass
import sqlite3

class CollectConnections():

    connections = []

    def __init__(self, connection):

        self.connection = connection
    
    @dataclass
    class Connection():

        connection: sqlite3.Connection

    def get_connection(self):

        c = self.Connection(self.connection)

        self.append_connection(c)

    @classmethod
    def append_connection(cls, c):

        cls.connections.append(c)

    @classmethod
    def clear_connections(cls):

        cls.connections.clear()

    