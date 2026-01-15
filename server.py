
from flask import Flask , request , jsonify

class Server():

    def __init__(self, host, port):

        self.app = Flask("POST_Pi")

        self.host = host

        self.port = port

        self.setup_routes()

    def setup_routes(self):

        @self.app.route("/send", ["POST"])
        def get_data():

            data = request.get_json()
            self.extract_data(data)
            return jsonify({"Success": "Thanks for you request!"}) , 200

    def extract_data(self, data):

        if "title" not in data:

            return jsonify({"Error": "Bad Request"}) , 400
        
        title = data["title"]

        if "message" not in data:

            return jsonify({"Error": "Bad Request"}) , 400

        message = data["message"]

    def run_server(self):

        self.app.run(self.host, self.port)


