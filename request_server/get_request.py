
import requests

url = "http://192.168.2.122:5000/get"

response = requests.get(url=url)
print(response.json())