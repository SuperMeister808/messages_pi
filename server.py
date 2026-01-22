
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

    def __init__(self, host, port, message_handler, message_reader):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.message_handler = message_handler

        self.message_reader = message_reader

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", methods=["POST"])
        def send_data():

                conn = sqlite3.connect("messages.db")

                if request.content_type != "application/json":
                    self.message_handler.clear_data()
                    self.close_connection(conn)
                    return jsonify({"Error": "Content Type application/json not found!"}) , 405
            
                try:
                    data = request.get_json()
                except BadRequest:
                    self.message_handler.clear_data()
                    self.close_connection(conn)
                    return jsonify({"Error": "Bad Request"}) , 400

                try:
                    title , message = self.message_handler.extract_data(data)
                except KeyError:
                    self.message_handler.clear_data()
                    self.close_connection(conn)
                    return jsonify({"Error": "Keys not found"}) , 405
                
                #for testing...
                try:
                    self.message_handler.collect_data(conn, title, message)
                except Exception as e:
                    self.message_handler.clear_data()
                    self.close_connection(conn)
                    return jsonify({"Error": f"{e}"}) , 400
                
                try:
                    self.message_handler.write_data(conn, title, message)
                except sqlite3.OperationalError:
                    self.message_handler.clear_data()
                    self.close_connection(conn)
                    return jsonify({"Error": "Table not found!"}) , 500
                
                self.message_handler.clear_data()
                self.close_connection(conn)
                return jsonify({"Success": "Thanks for you request!"}) , 200
        
        @self.app.route("/get", methods=["GET"])
        def get_data():
            
            conn = sqlite3.connect("messages.db")

            try:
                colums , rows = self.message_reader.get_table(conn)
            except sqlite3.OperationalError:
                self.close_connection(conn)
                return jsonify({"Error": "No table found!"}) , 405
            
            self.close_connection(conn)
            return jsonify({"colums": colums, "rows": rows})

    def close_connection(self, conn):

        conn.close()
    
    def run_server(self):

        self.app.run(self.host, self.port)


