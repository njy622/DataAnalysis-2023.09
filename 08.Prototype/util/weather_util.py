import requests

def get_weather(static_path, lat, lng):
    filename = f'{static_path}keys/OpenweatherApiKey.txt'
    with open(filename) as file:
        weather_key = file.read()
    base_url = 'https://api.openweathermap.org/data/2.5/onecall'
    url = f'{base_url}?lat={lat}&lon={lng}&appid={weather_key}&units=metric&lang=kr'
    result = requests.get(url).json()
    temp=result['current']['temp']
    desc = result['current']['weather'][0]['description']
    icon_code = result['current']['weather'][0]['icon']
    icon_url = f'http://api.openweathermap.org/img/w/{icon_code}.png'
    html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>
            온도: <strong>{temp:.1f}</strong>&#8451'''                  # &#8451 섭씨 도씨 의미
    return html