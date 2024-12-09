import json
import math

def generate_chart_data():
    data = {
        "x": [],
        "series": [],
        "exact": []
    }
    
    # Генерация значений x от 1.5 до 5.0 с шагом 0.1
    x_values = [x / 10 for x in range(15, 51)]  

    for x in x_values:
        if x <= 1:
            continue  # Пропускаем недопустимые значения
        
        # Точное значение функции
        exact_value = math.log((x + 1) / (x - 1))
        data["x"].append(x)
        data["exact"].append(exact_value)

        # Разложение в ряд до 10 членов
        series_value = sum(2 / ((2 * n + 1) * (x ** (2 * n + 1))) for n in range(10))
        data["series"].append(series_value)

    # Сохранение данных в JSON
    with open("chart_data.json", "w") as file:
        json.dump(data, file)

generate_chart_data()
