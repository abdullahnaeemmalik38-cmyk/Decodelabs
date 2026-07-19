import requests

url = "http://127.0.0.1:5000/check-password"

data = {
    "password": "hello123"
}

response = requests.post(url, json=data)

print(response.json())