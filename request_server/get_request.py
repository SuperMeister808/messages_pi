
import requests

url = "http://192.168.2.116:5000/get"

response = requests.get(url=url)
print(response.json())