from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
import correct_input


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        """
        Абстрактный метод для вычисления площади геометрической фигуры.
        """
        pass


class Color:
    def __init__(self, color):
        self.color = Color(color)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color


class Triangle(GeometricFigure):
    filename_save_fig = "task4/triangle.png"
    """
    Класс, представляющий треугольник.
    """
    figure_type = "Треугольник"

    def __init__(self, a, h, color, text):
        """
        Инициализация экземпляра треугольника.
        """
        self.a = a
        self.h = h
        self.text = text
        self.color = color

    def __str__(self):
        return f"{Triangle.figure_type} - фигура задания, подпись фигуры: {self.text}"

    def calculate_area(self):
        """
        Вычисляет площадь равнобедренного треугольника.
        """
        return self.a * self.h * 0.5

    def get_info(self):
        """
        Возвращает информацию о треугольнике.
        """
        return "{} - основание a: {}, высота h: {}, цвет: {}, площадь: {}".format(
            self.figure_type, self.a, self.h, self.color, round(self.calculate_area(), 2))

    def draw(self):
        """
        Рисует равнобедренный треугольник.
        Создает графическое представление треугольника и сохраняет его в файл.
        """
        # Создает объект фигуры (fig) и набор подграфиков (ax)
        fig, ax = plt.subplots()

        # Координаты вершин равнобедренного треугольника
        vertices = np.array([
            [0, 0],  # Левая нижняя вершина
            [self.a, 0],  # Правая нижняя вершина
            [self.a / 2, self.h]  # Верхняя вершина
        ])

        # Создание полигона на основе вершин
        triangle = plt.Polygon(vertices, closed=True, edgecolor='black', facecolor=self.color)

        # Добавление треугольника на график
        ax.add_patch(triangle)

        # Настройка осей и масштаба
        ax.set_xlim(-0.1 * self.a, self.a + 0.1 * self.a)
        ax.set_ylim(-0.1 * self.h, self.h + 0.1 * self.h)

        # Добавление подписей осей
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        # Добавление заголовка графика
        ax.set_title('Равнобедренный треугольник')

        # Добавление текста в центре треугольника
        ax.text(self.a / 2, self.h / 2, self.text, ha='center', va='center')

        # Сохранение графика в файл
        fig.savefig(self.filename_save_fig)

        # Отображение графика
        plt.show()



def task4():
    a = correct_input.validate_positive_float("Введите основание равнобедренного треугольника: ")
    h = correct_input.validate_positive_float("Введите высоту равнобедренного треугольника: ")
    text = input("подпись: ")
    color = correct_input.input_existing_color("Цвет: ")
    triangle = Triangle(a, h, color, text)
    print(triangle.get_info())
    print(triangle)
    triangle.draw()
