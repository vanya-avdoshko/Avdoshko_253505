# В соответствии с заданием своего варианта составить программу для анализа текста,
# вводимого с клавиатуры.

def my_decor(func):
    def foo():
        print("Ввод строки:")
        result = func()
        print("Программа вывела количество заглавных букв")
        return result
    return foo



@my_decor
def capital_counter():
    ''' This function count a number of capital letters in the row

        Keyword arguments:
            s - string of symbols

        Return value:
            count - a number of capital letters
    '''
    s = input("Enter the string: ")
    count = 0
    for i in s:
        count += 1 if i in 'QWERTYUIOPASDFGHJKLZXCVBNM' else 0
    print(count)
    return count
