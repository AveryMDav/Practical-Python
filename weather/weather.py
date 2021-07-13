import requests

def get_weather_desc_and_temp():
    api_key = "e2479bf1d2fe9248e4908cdb4ec90cdd"
    city = 'Colorado Springs'
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    request = requests.get(url)
    json = request.json()
    desc = json.get("weather")[0].get("description")
    temp_min = json.get('main').get("temp_min")
    temp_max = json.get('main').get("temp_max")
    return {'desc': desc,
            'temp_min': temp_min,
            'temp_max': temp_max}

def main():
    weather_dict = get_weather_desc_and_temp()
    print("Today's forcast is", weather_dict.get('desc'))
    print("The min temperature is", weather_dict.get('temp_min'))
    print("The max temperature is", weather_dict.get('temp_max'))

main()