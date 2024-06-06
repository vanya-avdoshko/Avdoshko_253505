'''
    Laboratory work № 4
        Variant 1
        Avdoshko Ivan, gr. 253505, 21.04.2024

This program was created for solving following tasks:
* putting a dictionary in a file
* a program for text analysis
* refinement of the function decomposition program in a row
* developing a geometric shape class and plotting its graph
* a program to explore the possibilities of the numpy library
'''


from Task1.task1 import task1
from Task2.text_analyzer import TextAnalyzer
from Task3.task3 import task3
from Task5.task5 import task5
from Task4.task4 import task4
import correct_input


def main():
    while True:
        print("1. Task 1\n2. Task 2\n3. Task 3\n4. Task 4\n5. Task 5\n6. Exit")
        choice = correct_input.validate_positive_int("Enter the number: ")
        if choice == 1:
            task1()

        elif choice == 2:
            analyzer: TextAnalyzer = TextAnalyzer('input_text.txt', 'analysis_results.txt')
            analyzer.analyze_text()

        elif choice == 4:
            task4()

        elif choice == 3:
            task3()

        elif choice == 5:
            task5()

        elif choice == 6:
            return 0

        else:
            print("ERROR")


if __name__ == "__main__":
    main()
