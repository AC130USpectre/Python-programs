from tkinter import *
from datetime import datetime
import requests

def parseWind(deg):
    if 22.5 < deg <= 67.5:
        return 'северо-восточный'
    elif 57.5 < deg <= 112.5:
        return 'восточный'
    elif 112.5 < deg <= 157.5:
        return 'юго-восточный'
    elif 157.5 < deg <= 202.5:
        return 'южный'
    elif 202.5 < deg <= 247.5:
        return 'юго-западный'
    elif 247.5 < deg <= 292.5:
        return 'западный'
    elif 292.5 < deg <= 337.5:
        return 'северо-западный'
    else:
        return 'северный'

def unixTimeConvert(unix_time):
    time = datetime.fromtimestamp(int(unix_time))
    return '{}:{}:{}'.format(time.hour, time.minute, time.second)

def parsePress(string):
    return str(int(string) * 0.7500637554192)[:5]

main = Tk()
def closeWindow():
    main.destroy()
main.protocol('WM_DELETE_WINDOW', closeWindow)
main.wm_title("Weather Wizard")

sitynameStr = StringVar()
sitynameStr.set('Moscow')
sityname = Entry(main, textvariable = sitynameStr)
sityname.grid(row = 1, column = 1)
sun = Label(main, text = 'Время восхода/захода солнца.')
sun.grid(row = 2, column = 1)
descr = Label(main, text = 'Описание погоды.')
descr.grid(row = 3, column = 1)
clouds = Label(main, text = 'Облачность.')
clouds.grid(row = 4, column = 1)
temp = Label(main, text = 'Температура.')
temp.grid(row = 5, column = 1)
temp_min = Label(main, text = 'Минимальная температура.')
temp_min.grid(row = 6, column = 1)
temp_max = Label(main, text = 'Максимальная температура.')
temp_max.grid(row = 7, column = 1)
press = Label(main, text = 'Давление.')
press.grid(row = 8, column = 1)
humid = Label(main, text = 'Влажность.')
humid.grid(row = 9, column = 1)
wind = Label(main, text = 'Ветер.')
wind.grid(row = 10, column = 1)

button = Button(main, text = 'Обновить')

def refresh(event):
    sityNameBuf = sityname.get()
    sitynameStr.set('Запрашиваю данные...')
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&APPID=7d2508466006b8b8c5082f0482f6ea27&units=metric&lang=ru'.format(sityNameBuf)).json()
    if 'name' in r:
        sitynameStr.set(r['name'])
    else:
        sitynameStr.set('Запрос данных завершён неудачно!')
    if 'sys' in r:
        if 'sunrise' in r['sys'] and 'sunset' in r['sys']:
            sun.config(text = 'Восход в ' + unixTimeConvert(r['sys']['sunrise']) + ', закат в ' + unixTimeConvert(r['sys']['sunset']) + '.')
        elif 'sunrise' in r['sys']:
            sun.config(text = 'Восход в ' + unixTimeConvert(r['sys']['sunrise']) + '.')
        elif 'sunset' in r['sys']:
            sun.config(text = 'Закат в ' + unixTimeConvert(r['sys']['sunset']) + '.')
        else:
            sun.config(text = 'Время восхода/захода солнца.')
    else:
        sun.config(text = 'Время восхода/захода солнца.')
    if 'weather' in r and 'description' in r['weather'][0]:
        descr.config(text = r['weather'][0]['description'].upper())
    else:
        descr.config(text = 'Описание погоды.')
    if 'clouds' in r and 'all' in r['clouds']:
        clouds.config(text = 'Облачность {}%.'.format(r['clouds']['all']))
    else:
        clouds.config(text = 'Облачность.')
    if 'main' in r:
        if 'temp' in r['main']:
            temp.config(text = str(r['main']['temp']) + u' \u00B0' + 'C')
        else:
            temp.config(text = 'Температура.')
        if 'temp_min' in r['main']:
            temp_min.config(text = 'От ' + str(r['main']['temp_min']) + u' \u00B0' + 'C')
        else:
            temp_min.config(text = 'Минимальная температура.')
        if 'temp_max' in r['main']:
            temp_max.config(text = 'До ' + str(r['main']['temp_max']) + u' \u00B0' + 'C')
        else:
            temp_max.config(text = 'Максимальная температура.')
        if 'pressure' in r['main']:
            press.config(text = '{} кПа, {} мм. рт. ст.'.format(r['main']['pressure'] / 10, parsePress(r['main']['pressure'])))
        else:
            press.config(text = 'Давление.')
        if 'humidity' in r['main']:
            humid.config(text = 'Влажность {}%.'.format(str(r['main']['humidity'])))
        else:
            humid.config(text = 'Влажность.')
    else:
        temp.config(text = 'Температура.')
        temp_min.config(text = 'Минимальная температура.')
        temp_max.config(text = 'Максимальная температура.')
        press.config(text = 'Давление.')
        humid.config(text = 'Влажность.')
    if 'wind' in r:
        if 'deg' and 'speed' in r['wind']:
            wind.config(text = 'Ветер {}, скорость {}.'.format(parseWind(r['wind']['deg']), str(r['wind']['speed']) + ' м/с'))
        elif 'deg' in r['wind']:
            wind.config(text = 'Ветер {}.'.format(r['wind']['deg']))
        elif 'speed' in r['wind']:
            wind.config(text = 'Cкорость {}.'.format(str(r['wind']['speed']) + 'м/с'))
        else:
            wind.config(text = 'Ветер.')
    else:
        wind.config(text = 'Ветер.')

button.bind('<Button-1>', refresh)
button.grid(row = 11, column = 1)
main.mainloop()
