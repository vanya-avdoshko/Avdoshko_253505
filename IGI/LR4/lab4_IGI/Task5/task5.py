import numpy as np
import correct_input


class NumPyOperations:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = None

    def __str__(self):
        if self.matrix is not None:
            return f"Количество строк: {self.n}, количество столбцов: {self.m}.\nИсходная матрица:\n{self.matrix}"
        else:
            return f"Матрица еще не создана."

    def create_matrix(self, min=0, max=100):
        self.matrix = np.random.randint(min, max, size=(self.n, self.m))

    def create_zeros(self):
        self.matrix = np.zeros((self.n, self.m))

    def create_ones(self):
        self.matrix = np.ones((self.n, self.m))

    def create_full(self, value):
        self.matrix = np.full((self.n, self.m), value)

    def create_eye(self):
        self.matrix = np.eye(self.n)

    def create_arange(self, start, stop, step=1):
        self.matrix = np.arange(start, stop, step)

    def __getitem__(self, index):
        return self.matrix[index]

    def __setitem__(self, index, value):
        self.matrix[index] = value

    def __add__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix + other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix + other
        else:
            print("Неподдерживаемый тип операнда для сложения.")
            return self.matrix
        return result

    def __sub__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix - other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix - other
        else:
            print("Неподдерживаемый тип операнда для вычитания.")
            return self.matrix
        return result

    def __mul__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix * other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix * other
        else:
            print("Неподдерживаемый тип операнда для умножения.")
            return self.matrix
        return result

    def __truediv__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = self.matrix / other.matrix
        elif isinstance(other, (int, float)):
            result.matrix = self.matrix / other
        else:
            print("Неподдерживаемый тип операнда для деления.")
            return self.matrix
        return result

    def __pow__(self, other):
        result = NumPyOperations(self.n, self.m)
        if isinstance(other, NumPyOperations):
            result.matrix = np.power(self.matrix, other.matrix)
        elif isinstance(other, (int, float)):
            result.matrix = np.power(self.matrix, other)
        else:
            print("Неподдерживаемый тип операнда для возведения в степень.")
            return self.matrix
        return result

    def sqrt(self):
        result = NumPyOperations(self.n, self.m)
        result.matrix = np.sqrt(self.matrix)
        return result

    def abs(self):
        result = NumPyOperations(self.n, self.m)
        result.matrix = np.abs(self.matrix)
        return result


class MatrixStatistics(NumPyOperations):
    def __init__(self, n, m):
        super().__init__(n, m)

    def mean(self):
        return np.mean(self.matrix)

    def median(self):
        return np.median(self.matrix)

    def corrcoef(self):
        return np.corrcoef(self.matrix)

    def var(self):
        return np.var(self.matrix)

    def std(self):
        return np.std(self.matrix)

    def find_column_with_min_sum(self):
        """Нахождение столбца с наименьшей суммой элементов."""
        column_sums = np.sum(self.matrix, axis=0)
        min_sum_column_index = np.argmin(column_sums)
        return min_sum_column_index

    def calculate_column_median_standard(self, column_index):
        """Вычисление медианы с использованием стандартной функции."""
        return np.median(self.matrix[:, column_index])

    def calculate_column_median_custom(self, column_index):
        """Вычисление медианы через программирование формулы."""
        sorted_column = np.sort(self.matrix[:, column_index])
        n = len(sorted_column)
        if n % 2 == 0:
            return (sorted_column[n // 2 - 1] + sorted_column[n // 2]) / 2
        else:
            return sorted_column[n // 2]



def task5():
    n = correct_input.validate_positive_int("Введите количество строк в матрице: ")
    m = correct_input.validate_positive_int("Введите количество столбцов в матрице: ")
    arr1 = MatrixStatistics(n, m)
    arr1.create_matrix()
    print(arr1)
    # arr1 = arr1 + 2
    print()
    print(f"Cредние значения всех элементов матрицы: {arr1.mean()}")
    print(f"Медиана матрицы: {arr1.median()}")
    print(f"Коэффициент корреляции между элементами матрицы:\n{arr1.corrcoef()}")
    print(f"Дисперсии всех элементов матрицы {arr1.var()}")
    print(f"Стандартного отклонения всех элементов матрицы: {arr1.std()}")
    print()
    index = arr1.find_column_with_min_sum()
    print(f"Столбец с наименьшей суммой элементов: {index}")
    # arr1 = arr1.sqrt()
    print(f"Медиана столбца матрицы с наименьшей суммой элементов (программированием формулы): {arr1.calculate_column_median_custom(index)}")
    print(f"Медиана столбца матрицы с наименьшей суммой элементов: {arr1.calculate_column_median_standard(index)}")
