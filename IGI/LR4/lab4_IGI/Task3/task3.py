from tabulate import tabulate
import statistics
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
import math


class FunctionDecomposition():
    def __init__(self):
        self.x, self.epsilon = self.get_input_values()
        self.results = []
        self.values = []

    def __str__(self):
        return f"Значение x: {self.x}, значение epsilon: {self.epsilon}, последовательность разложения: {self.values}"

    @property
    def xValue(self):
        return self.x

    @xValue.setter
    def xValue(self, x):
        self.x = x

    @property
    def epsilonValue(self):
        return self.epsilon

    @epsilonValue.setter
    def epsilonValue(self, epsilon):
        self.epsilon = epsilon

    def get_input_values(self):
        """
        Получает значения аргумента x и точности epsilon от пользователя.
        Проверяет их на правильность ввода и возвращает их.
        Если значение аргумента x находится за пределами допустимого интервала (|x| > 1),
        функция выводит сообщение об ошибке и требует повторный ввод данных.
        Если значение точности epsilon отрицательное, функция также выводит
        сообщение об ошибке и требует повторный ввод данных.
        """
        while True:
            try:
                x = float(input("Введите значение аргумента x (|x| > 1): "))
                if -1 <= x <= 1:
                    print("Недопустимый аргумент")
                    continue
                epsilon = float(input("Введите желаемую точность вычислений epsilon: "))
                if epsilon < 0:
                    print("Значение должно быть > 0")
                    continue
            except ValueError:
                print("Ошибка ввода")
                continue
            return x, epsilon

    def calculate_function(self):
        """
        Выполняет разложение функции в степенной ряд для заданных значения аргумента x и точности epsilon.
        Заполняет списки x_values, series_values и math_values значениями аргумента, значениями разложения функции
        и значениями функции, вычисленными с помощью модуля math соответственно.

        Цикл выполняется, пока на какой-то итерации значении переменной degree будет меньше значения epsilon либо когда
        не будет достигнуто 500 итераций
        """
        x = self.x
        self.results = []
        self.values = []
        res = 0.0
        counter = 0
        n = 500
        for i in range(n):
            temp = 2 / ((2 * i + 1) * (x ** (2 * i + 1)))
            if abs(temp) > abs(self.epsilon):
                res += temp
                self.values.append(temp)
                self.results.append(res)
                counter += 1
            else:
                break

        data = [[x, counter, res, math.log((x + 1) / (x - 1)), self.epsilon]]
        headers = ["x", "n", "F(x)", "Math F(x)", "eps"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def print_sequence(self):
        print(self.values)


class AnalyzeFunc(FunctionDecomposition):
    file_decompose = "task3/sequence_fun.png"
    file_main_fun = "task3/main_fun.png"

    def __init__(self):
        super().__init__()

    def avarage_sequence(self):
        if len(self.values) == 0:
            return None
        return np.mean(self.values)

    def median_sequence(self):
        if len(self.values) == 0:
            return None
        return np.median(self.values)

    def mode_sequence(self):
        if len(self.values) == 0:
            return None
        return stats.mode(self.values).mode[0]

    def variance_sequence(self):
        if len(self.values) == 0:
            return None
        return np.var(self.values)

    def calculate_standard_deviation(self):
        if len(self.values) == 0:
            return None
        return np.std(self.values)

    def draw_fun(self):
        # Создаем диапазон значений x, такие что |x| > 1
        x_left = np.linspace(-5, -1.01, 250)  # Значения x < -1
        x_right = np.linspace(1.01, 5, 250)  # Значения x > 1
        x = np.concatenate((x_left, x_right))

        # Вычисляем значение функции ln((x + 1) / (x - 1))
        y = np.log((1 + x) / (x - 1))
        idx1 = np.abs(x + 1).argmin()
        idx2 = np.abs(x - 1).argmin()
        y[idx1] = np.nan
        y[idx2] = np.nan

        # Создаем график
        plt.plot(x, y, color='black', linewidth=2)
        plt.legend(['График функции'])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График функции ln((x + 1) / (x - 1))')

        # Добавляем сетку
        plt.grid(True)

        # Сохраняем график
        plt.savefig(self.file_main_fun)

        # Отображаем график
        plt.show()

    def draw_sequence(self):
        # Создаем график последовательности разложения
        plt.plot(range(1, len(self.results) + 1), self.results, label=f'x={self.x:.2f}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График последовательности разложения')
        plt.grid(True)

        # Сохраняем график
        plt.savefig(self.file_decompose)

        # Отображаем график
        plt.show()

def task3():
    func = AnalyzeFunc()
    func.calculate_function()
    func.draw_sequence()
    func.draw_fun()
    func.print_sequence()
    print(f"Среднее арифметическое элементов последовательности: {func.avarage_sequence()}")
    print(f"Медиана последовательности: {func.median_sequence()}")
    print(f"Мода последовательности: {func.mode_sequence()}")
    print(f"Дисперсия последовательности: {func.variance_sequence()}")
    print(f"СКО последовательности: {func.calculate_standard_deviation()}")
