# we use the right library

import requests

city = input("Enter Your city: ")

# downloading page by get


res = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid=dbed2c52ca15d6395ec6241e25d4a536&units=metric'.format(city))
data = res.json()

# choosing weather parameters from data
# first sqare bracker show category, second value


temp = data["main"]["temp"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]


# Puting data to weather desciption by format function


print("Temperature: ", temp)
print("Wind speed: {}".format(wind_speed))
print("Description: {}".format(description))

