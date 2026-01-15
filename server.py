
from flask import Flask , request , jsonify
from werkzeug.exceptions import BadRequest

from title import CollectTitel
from message import CollectMessage

class Server():

    def __init__(self, host, port):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", methods=["POST"])
        def get_data():

            try:
                data = request.get_json()
            except BadRequest:
                return jsonify({"Error": "Bad Request"}) , 400
            
            try:
                title , message = self.extract_data(data)
            except KeyError:
                return jsonify({"Error": "Keys not found"}) , 405
            
            self.collect_data(title, message)
            self.clear_data()
            
            return jsonify({"Success": "Thanks for you request!"}) , 200

    def extract_data(self, data):

        title = data["title"]
        message = data["message"]
        
        return title , message

        
    def collect_data(self, title, message):

        t = CollectTitel(title)   
        m = CollectMessage(message)

        t.collect_title()
        m.collect_messages()

    def clear_data(self):

        t = CollectTitel("not relevant")
        m = CollectMessage("not relevant")

        t.clear_titles()
        m.clear_messages()


    def run_server(self):

        self.app.run(self.host, self.port)


