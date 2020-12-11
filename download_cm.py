import requests
import sys

url = sys.argv[1]
target_path = sys.argv[2]

response = requests.get(url, stream=True)
if response.status_code == 200:
    with open(target_path, 'wb') as f:
        f.write(response.raw.read())