from task4.data import word_list


def words_counter():
    '''This function count a number of words in the string

        Keyword arguments:
            word_list - a sentence
    '''
    count = len(word_list)
    print("Number of words: ", count)
