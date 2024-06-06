from task4.data import word_list

def longest_word():
    '''This function found the longest word and his position's number in the sentence
            Keyword arguments:
                word_list - a sentence
    '''
    long_word = max(word_list, key=len)
    print("The longest word: ", long_word, "\nHis position: ", word_list.index(long_word) + 1)
