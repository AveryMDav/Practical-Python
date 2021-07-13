import requests

api_key = 'e2479bf1d2fe9248e4908cdb4ec90cdd'
city = "Orlando"
url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'R&appid='+api_key

request = requests.get(url)
json = request.json()
print(json)