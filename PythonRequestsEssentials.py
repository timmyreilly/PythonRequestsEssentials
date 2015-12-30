import requests
import json

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are = 'working')

r = requests.get(url, cookies=cookies)

r.text 

r = requests.get('http://httpbin.org/stream/4', stream=True)
for line in r.iter_lines():
    if line: 
        print(json.loads(line))


# doing linky stuff

url = "https://api.github.com/search/code?q=addClass+user:mozilla&page=1&per_page=4"

response = requests.head(url=url)
response.headers['link']
