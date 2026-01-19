
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

            with sqlite3.connect("messages.db") as conn:
            
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
            
                self.collect_data(titel, message, conn)
                self.write_data_on_database(conn)
                self.clear_data()
            
                return jsonify({"Success": "Thanks for you request!"}) , 200

    def extract_data(self, data):

        titel = data["titel"]
        message = data["message"]
        
        return titel , message

        
    def collect_data(self, titel, message, conn):

        t = CollectTitel(titel)   
        m = CollectMessage(message)
        c = CollectConnections(conn)

        c.collect_connection()
        t.collect_title()
        m.collect_messages()

    def write_data_on_database(self, conn):

        d = Database()
        d.add_message(conn, CollectTitel.titels[-1].titel, CollectMessage.messages[-1].message)
    
    def clear_data(self):

        t = CollectTitel("not relevant")
        m = CollectMessage("not relevant")
        c = CollectConnections("not relevant")

        t.clear_titles()
        m.clear_messages()
        c.clear_connections()


    def run_server(self):

        self.app.run(self.host, self.port)


