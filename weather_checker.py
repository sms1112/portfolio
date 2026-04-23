import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "2d3e7f8a9b1c4d6e7f8a9b1c4d6e7f8a" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"
    try:
        data = requests.get(url).json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        return f"🌤️ {city}: {temp}°C, {desc}"
    except:
        return "Город не найден"

def show_weather():
    city = entry.get()
    if city:
        result = get_weather(city)
        label.config(text=result)
    else:
        messagebox.showwarning("Ошибка", "Введи город!")

root = tk.Tk()
root.title("Погода — Junior Dev")
root.geometry("400x300")

tk.Label(root, text="Город:").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)
entry.insert(0, "Москва")

tk.Button(root, text="Узнать погоду", command=show_weather, bg="#007bff", fg="white").pack(pady=10)
label = tk.Label(root, text="Результат здесь", font=("Arial", 12))
label.pack(pady=20)

root.mainloop()
