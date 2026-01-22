
import requests
import sys
import json

def post_request(data):
    
    url = "http://192.168.2.126:5000/send"

    response = requests.post(url=url, json=data)

    print(response.json())

if __name__ == "__main__":

    if len(sys.argv) > 1:

        data_json_string = sys.argv[1]
        data = json.loads(data_json_string)
    
        post_request(data)
    else:
        print({"Error": "No arguments found!"})