import requests

response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1":"Test title"})
print(response.text)