# Организовать цикл, который принимает целые числа с клавиатуры и суммирует их квадраты.
# Окончание цикла – ввод числа 0
def square_sum():
    ''' this function calculate a sum of squares of integers

        Keyword arguments:
            x - integer number
    '''
    try:
        x = int(input("Enter the number (0 to stop): "))
        res = 0
        while x:
            res += x ** 2
            x = int(input("Enter the number (0 to stop): "))
    except ValueError:
        print("ERROR")
    else:
        print("Sum of squares: ", res)
