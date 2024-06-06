import math


def log():
    '''function for decomposing ln((x+1)/(x-1)) into a power series

        Keyword arguments:
            x - argument's value
            eps - accuracy of calculations
    '''
    res = 0.0
    counter = 0
    n = 500
    try:
        x = float(input("Enter x (|x|>1): "))
        math_result = math.log((x + 1) / (x - 1))
        eps = float(input("Enter eps: "))
    except ZeroDivisionError:
        print("ERROR")
    except ValueError:
        print("ERROR")
    else:
        table = []
        for i in range(n):
            temp = 2 / ((2 * i + 1) * (x ** (2 * i + 1)))
            if abs(temp) > abs(eps):
                res += temp
                counter += 1
                table.append((x, i, res, math_result, eps))  # Добавляем кортеж в список
            else:
                break

        if table:
            last_row = table[-1]  # Получаем последнюю строку из списка
            x, n, value, math_value, eps = last_row
            print("x\t| n\t| F(x)\t\t| Math F(x)\t| eps")
            print("----------------------------------------------")
            print(f"{x}\t| {n}\t| {value:.5f}\t| {math_value:.5f}\t| {eps}")
        else:
            print("Таблица пуста.")

        print("the number of series members required to achieve the specified calculation accuracy:", counter)
