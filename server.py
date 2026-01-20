
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

                conn = sqlite3.connect("messages.db")

                if request.content_type != "application/json":

                    return jsonify({"Error": "Content Type application/json not found!"}) , 405
            
                try:
                    data = request.get_json()
                except BadRequest:
                    self.close_connection(conn)
                    return jsonify({"Error": "Bad Request"}) , 400
            
                data["conn"] = conn

                try:
                    self.extract_data(data)
                except KeyError:
                    self.close_connection(conn)
                    return jsonify({"Error": "Keys not found"}) , 405
                
                self.clear_data()
                self.close_connection(conn)

                return jsonify({"Success": "Thanks for you request!"}) , 200
    
    def extract_data(self, data):

        conn = data["conn"]
        titel = data["titel"]
        message = data["message"]
        
        #for Testing...
        self.collect_data(conn, titel, message)
        
        self.write_data_on_database(conn, titel, message)

    def collect_data(self, conn, titel, message):


        t = CollectTitel(titel)   
        m = CollectMessage(message)
        c = CollectConnections(conn)
        
        t.collect_title()
        m.collect_messages()
        c.collect_connection()

    def write_data_on_database(self, conn, titel, message):
        
        d = Database(conn)
        d.add_message(titel, message)
 
    def clear_data(self):

        CollectConnections.clear_connections()
        CollectMessage.clear_messages()
        CollectTitel.clear_titles()

    def close_connection(self, conn):

        conn.close()
    
    def run_server(self):

        self.app.run(self.host, self.port)


