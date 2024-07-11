import requests
import tkinter as tk
import json

def get_weather():
    API = '9d5ce9cedfe586c9dc707f88e1350ed7'
    city = weather.get()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        
        label_weather = tk.Label(windows, text=f'Сейчас погода: {int(temp)}℃')
        label_weather.place(relx=0.25, rely=0.50)
    
    if res.status_code != 200:
        label_weather = tk.Label(windows, text=f'Город {city.title()} не найден')
        label_weather.place(relx=0.20, rely=0.50)

windows = tk.Tk()
windows.title('Погода')
windows.geometry('249x320')

weather = tk.Entry()
label = tk.Label(windows, text='Ведите город где хотите узнать погоду')
button = tk.Button(windows, text='Узнать погоду', command=get_weather)



weather.place(relx=0.2, rely=0.2)
label.place(relx=0.05, rely=0.1)
button.place(relx=0.25, rely=0.3)
windows.resizable(False, False)
windows.mainloop()