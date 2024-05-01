import requests
import json

if __name__ == '__main__':
    url = 'http://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=2))
