from task4.data import word_list

def even_word():
    '''This function print all even words in the sentence

        Keyword arguments:
            word_list - a sentence
    '''
    for i in range(1, len(word_list), 2):
        print(word_list[i])
