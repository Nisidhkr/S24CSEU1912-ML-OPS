import urllib.request
import json

url = f"https://api.github.com/users/Nisidhkr/repos?per_page=100"

response = urllib.request.urlopen(url)

data = json.loads(response.read())

print("Number of repositories:", len(data))
