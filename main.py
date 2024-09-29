import tkinter as tk
import requests

# Получаем координаты города (широта и долгота)

def get_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
    headers = {
        'User-Agent': 'MyWeatherApp/1.0'  # Укажите здесь название вашего приложения
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data)
    if data:
        return float(data[0]['lat']), float(data[0]['lon'])
    else:
        return None, None


# Получаем погоду с Open-Meteo по координатам
def get_weather(city):
    lat, lon = get_coordinates(city)
    if lat is not None and lon is not None:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        response = requests.get(url)
        data = response.json()
        if 'current_weather' in data:
            return f"Температура в {city}: {data['current_weather']['temperature']}°C"
        else:
            return "Погода не найдена"
    else:
        return "Город не найден"

# Показываем погоду
def show_weather():
    city = city_entry.get()
    result = get_weather(city)
    result_label.config(text=result)

# Создаем окно
root = tk.Tk()
root.title("Погода по городу")
root.geometry("400x300")  # Устанавливаем размер окна

# Поле для ввода города
tk.Label(root, text="Введите город:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

# Кнопка для показа погоды
tk.Button(root, text="Показать погоду", command=show_weather).pack()

# Поле для вывода результата
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
