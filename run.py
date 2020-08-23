import requests
city = input("Enter Your city: ")
res = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=dbed2c52ca15d6395ec6241e25d4a536&units=metric'.format(city))
data = res.json()
temp = data["main"]["temp"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

print("Temperature: ", temp)
print("Wind speed: {}".format(wind_speed))
print("Description: {}".format(description))
