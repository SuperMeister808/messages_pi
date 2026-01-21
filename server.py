
from flask import Flask , request , jsonify
from werkzeug.exceptions import BadRequest

from title import CollectTitle
from message import CollectMessage
from database import Database
from connections import CollectConnections

import sqlite3

import io

import json

class Server():

    def __init__(self, host, port):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", methods=["POST"])
        def send_data():

                conn = sqlite3.connect("messages.db")

                if request.content_type != "application/json":

                    self.close_connection(conn)
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
        
        @self.app.route("/get", methods=["GET"])
        def get_data():
            
            conn = sqlite3.connect("messages.db")

            try:
                colums , rows = self.get_table(conn)
            except sqlite3.OperationalError:
                self.close_connection(conn)
                return jsonify({"Error": "No table found!"}) , 405
            
            self.close_connection(conn)
            return jsonify({"colums": colums, "rows": rows})
            
    def get_table(self, conn):

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM messages")

        colums = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()

        return colums , rows

    #user can do it itself ...
    #def create_file(self, colums, rows):
        
    #    data = {"colums": colums, "rows": rows}
        
    #    buffer = io.BytesIO(json.dumps(data).encode("utf-8"))
    #    buffer.seek(0)

    #    return buffer
    
    def extract_data(self, data):

        conn = data["conn"]
        title = data["title"]
        message = data["message"]
        
        #for Testing...
        self.collect_data(conn, title, message)
        
        self.write_data(conn, title, message)

    def collect_data(self, conn, title, message):


        t = CollectTitle(title)   
        m = CollectMessage(message)
        c = CollectConnections(conn)
        
        t.collect_title()
        m.collect_messages()
        c.collect_connection()

    def write_data(self, conn, title, message):
        
        d = Database(conn)
        d.add_message(title, message)
 
    def clear_data(self):

        CollectConnections.clear_connections()
        CollectMessage.clear_messages()
        CollectTitle.clear_titles()

    def close_connection(self, conn):

        conn.close()
    
    def run_server(self):

        self.app.run(self.host, self.port)


