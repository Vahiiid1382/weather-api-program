import requests
import json
import pprint
flag = True
print('Hello welcome to weather app we have very information about weather of citys around the world!!!')
while flag:
    
    city_name = input('witch city do tou want to know?')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=13b9ce10cc8d9a63336857063b618625'
    result1 = requests.get(url)
    result2 = json.loads(result1.text)
    #print(result2)

    weather_main = result2['weather'][0]['description']
    now_temp = float(result2['main']['temp']) - 273.15
    humity = str(result2['main']['humidity']) + '%'
    wind_speed = str(result2['wind']['speed']) + 'm/s'
    print('Weather dis: ',weather_main)
    print('Right now temp: ',now_temp)
    print('Humidity percent: ',humity)
    print('Wind-speed: ',wind_speed)
    while True:
        edame = input('Do you want to continue?y/n')
        if edame == 'y':
            break
        elif edame == 'n':
            flag = False
            break
        else:
            print('Please enter right!!!y/n')
            continue
print('.....END........')
'''
'''
'''
'''