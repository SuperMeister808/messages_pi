
from flask import Flask , request , jsonify
from werkzeug.exceptions import BadRequest

from title import CollectTitel
from message import CollectMessage
from database import Database
from connections import CollectConnections

import sqlite3

class Server():

    def __init__(self, host, port):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", methods=["POST"])
        def get_data():

<<<<<<< HEAD
            with sqlite3.connect("messages.db") as conn:
=======
                conn = sqlite3.connect("messages.db")
>>>>>>> update_database
            
                if request.content_type != "application/json":

                    return jsonify({"Error": "Content Type application/json not found!"}) , 405
            
                try:
                    data = request.get_json()
                except BadRequest:
                    return jsonify({"Error": "Bad Request"}) , 400
            
                try:
                    titel , message = self.extract_data(data)
                except KeyError:
                    return jsonify({"Error": "Keys not found"}) , 405
            
<<<<<<< HEAD
                self.collect_data(titel, message, conn)
                self.write_data_on_database(conn)
                self.clear_data()
            
=======
                self.collect_data(conn, titel, message)
                self.write_data_on_database(conn)
                self.clear_data()
            
                self.close_connection(conn)
                
>>>>>>> update_database
                return jsonify({"Success": "Thanks for you request!"}) , 200

    def extract_data(self, data):

        titel = data["titel"]
        message = data["message"]
        
        return titel , message

        
<<<<<<< HEAD
    def collect_data(self, titel, message, conn):
=======
    def collect_data(self,conn, titel, message):
>>>>>>> update_database

        t = CollectTitel(titel)   
        m = CollectMessage(message)
        c = CollectConnections(conn)

        c.collect_connection()
        t.collect_title()
        m.collect_messages()
        c.collect_connection()

    def write_data_on_database(self, conn):
<<<<<<< HEAD

        d = Database()
        d.add_message(conn, CollectTitel.titels[-1].titel, CollectMessage.messages[-1].message)
=======

        d = Database(conn)

        d.add_message(CollectTitel.titels[-1].titel, CollectMessage.messages[-1].message)
>>>>>>> update_database
    
    def clear_data(self):

        t = CollectTitel("not relevant")
        m = CollectMessage("not relevant")
        c = CollectConnections("not relevant")

        t.clear_titles()
        m.clear_messages()
        c.clear_connections()

    def close_connection(self, conn):

        conn.close()
    
    def run_server(self):

        self.app.run(self.host, self.port)


