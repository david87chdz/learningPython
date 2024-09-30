import requests

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python"}
)
# Para ver los headers respone.headers
print(response.json())

data = response.json()
print(data.keys())