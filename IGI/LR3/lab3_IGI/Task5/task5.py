from Task5.task5_fun1 import init_list
from Task5.task5_fun1 import print_list
from Task5.task5_fun1 import my_generator

def main_task():
    '''
    This function calculate a sum of negative elements in the list and a product
    of elements between min and max elements. The list items are initialized by user.

        Keyword arguments:
            num - number of elements in the list
    '''
    try:
        num = int(input("Enter the number of elements: "))
    except ValueError:
        print("ERROR")
    else:
        f_list = init_list(num)

        sum = 0.0
        if len(f_list) != 0:
            print_list(f_list)
            for i in range(num):
                sum += f_list[i] if f_list[i] < 0 else 0

            min_index = f_list.index(min(f_list))
            max_index = f_list.index(max(f_list))

            start_index = min(min_index, max_index)
            end_index = max(min_index, max_index)

            product = 1

            for i in range(start_index + 1, end_index):
                product *= f_list[i]
            if end_index - start_index == 1:
                print("Sum of negative elements: ", sum, "\nThere is no elements between min and max elements")
            else:
                print("Sum of negative elements: ", sum, "\nProduct of elements between min and max: ", product)

def main_task_gen():
    '''This function calculate a sum of negative elements in the list and a product
    of elements between min and max elements. Еhe list items are initialized by the generator

        Keyword arguments:
            num - number of elements in the list
    '''

    try:
        num = int(input("Enter the number of elements: "))
    except ValueError:
        print("ERROR")
    else:
        f_list = []
        for i in my_generator(num):
            f_list.append(i)

        print_list(f_list)
        sum = 0.0

        for i in range(num):
            sum += f_list[i] if f_list[i] < 0 else 0

        min_index = f_list.index(min(f_list))
        max_index = f_list.index(max(f_list))

        start_index = min(min_index, max_index)
        end_index = max(min_index, max_index)
        if end_index - start_index == 1:
            print("There is no elements between min and max elements")

        product = 1

        for i in range(start_index + 1, end_index):
            product *= f_list[i]

        print("Sum of negative elements: ", sum, "\nProduct of elements between min and max: ", product)

