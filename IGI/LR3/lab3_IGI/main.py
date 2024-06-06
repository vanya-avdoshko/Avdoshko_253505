import task1, task2, task3
from task4.task4_1 import words_counter
from task4.task4_2 import longest_word
from task4.task4_3 import even_word
from Task5.task5 import main_task
from Task5.task5 import main_task_gen
import repetition
'''
    Laboratory work № 3: "Standard data types, collections, functions, modules"
            Developer: Avdoshko Ivan, group 253505
            Date of development: 27.03.2024

This program was created to solve the following tasks:
decomposing ln((x+1)/(x-1)) into a power series,
calculating a sum of squares of integers,
counting a number of capital letters in the row,
counting a number of words in the string,
founding the longest word and his position's number in the sentence,
printing all even words in the sentence,
calculating a sum of negative elements in the list and a product of elements between min and max elements.
'''
check = 1

while check:
    print("1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Exit")
    try:
        choice = int(input("Выберите пункт: "))
    except ValueError:
        print("ERROR")
        check = repetition.rep()
        continue

    if choice == 1:
        task1.log()

    elif choice == 2:
        task2.square_sum()

    elif choice == 3:
        task3.capital_counter()

    elif choice == 4:
        words_counter()
        longest_word()
        even_word()

    elif choice == 5:
        print("Sequence initialization: using a generator function or user input?")
        print("1. User input\n2. Generator function")
        try:
            choice2 = int(input())
        except ValueError:
            print("ERROR")
            check = repetition.rep()
            continue
        if choice2 == 1:
            main_task()
        elif choice2 == 2:
            main_task_gen()
        else:
            print("ERROR")
    elif choice == 6:
        break
    else:
        print("ERROR")

    check = repetition.rep()
