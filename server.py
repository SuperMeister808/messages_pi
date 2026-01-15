
from flask import Flask , request , jsonify
from werkzeug.exceptions import BadRequest

class Server():

    def __init__(self, host, port):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", ["POST"])
        def get_data():

            try:
                data = request.get_json()
            except BadRequest:
                return jsonify({"Error": "Bad Request"}) , 400
            
            self.extract_data(data)
            return jsonify({"Success": "Thanks for you request!"}) , 200

    def extract_data(self, data):
        
        try:
            title = data["title"]

            message = data["message"]
        except KeyError:
            return jsonify({"Error": "Keys not found"}) , 405

    def run_server(self):

        self.app.run(self.host, self.port)


