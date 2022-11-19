import urllib.request
import requests


opener = urllib.request.build_opener()
response = opener.open("https://httpbin.org/get")

print(response.read())

response = requests.get("https://httpbin.org/get")
print(response.text)