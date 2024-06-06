import random


def my_generator(n):
    '''
    This function generate random float numbers in range (-100; 100)

        Keyword arguments:
            n - number of elements
    '''
    for _ in range(n):
        yield random.uniform(-100, 100)


def init_list(num):
    '''This function is used to initialize the list

        Keyword arguments:
             num - number of arguments

        Returned value:
            float_list - list of float elements
    '''
    float_list = []
    try:
        for i in range(num):
            float_list.append(float(input("Enter the number: ")))
    except ValueError:
        print('ERROR')
    return float_list


def print_list(float_list):
    '''This function is used to print a list

        Keyword arguments:
              float_list - list of float elements
     '''
    print(float_list)
