import re
import zipfile

class TextAnalyzer:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_text(self):
        '''Чтение текста из файла'''
        with open(self.input_file, 'r', encoding='utf-8') as file:
            text = file.read()
            return text

    @staticmethod
    def count_sentences(text):
        '''Подсчет количества предложений в тексте '''
        sentences = re.split(r'(?<=[.!?]) +', text)
        return len(sentences)

    def count_sentence_types(self, text):
        '''Подсчет количества повествовательных, вопросительных и побудительных предложений в тексте'''
        narrative_sentences = re.findall(r'[A-Z][^.!?]*\.+', text)
        interrogative_sentences = re.findall(r'[A-Z][^.!?]*\?', text)
        imperative_sentences = re.findall(r'[A-Z][^.!?]*!', text)
        return len(narrative_sentences), len(interrogative_sentences), len(imperative_sentences)

    def average_sentence_length(self, text):
        '''Средняя длина предложения '''
        sentences = re.split(r'(?<=[.!?]) +', text)
        total_characters = sum(len(sentence) for sentence in sentences)
        total_sentences = len(sentences)
        return total_characters / total_sentences if total_sentences > 0 else 0

    def average_word_length(self, text):
        '''Средняя длина слова'''
        words = re.findall(r'\b\w+\b', text)
        total_characters = sum(len(word) for word in words)
        return total_characters / len(words)

    def count_smileys(self, text):
        '''Подсчет количетсва смайликов в тексте'''
        smileys = re.findall(r'[;:]-*[\(\[\)\]]+', text)
        return len(smileys)

    def find_all_capital_letters(self, text):
        '''Нахождение всех заглавных букв в тексте'''
        capital_letters = re.findall(r'[A-Z]', text)
        return capital_letters

    def replace_sequence(self, text):
        '''Замена буквосочетаний на qqq'''
        replaced_text = re.sub(r'([aA]+)(b+)([cC]+)', r'qqq', text)
        return replaced_text

    def count_words_max_length(self, text):
        '''Подсчет количества слов максимальной длины'''
        words = re.findall(r'\b\w+\b', text)
        max_word_length = max(len(word) for word in words)
        return sum(1 for word in words if len(word) == max_word_length)

    def find_words_with_punctuation(self, text):
        '''Поиск слов, после которых установлены точка или запятая'''
        words_with_punctuation = re.findall(r'\b\w+[,.]', text)
        return words_with_punctuation

    def find_longest_word_ending_with_e(self, text):
        '''Поиск самого длинного слова, оканчивающегося на е'''
        words = re.findall(r'\b\w+\b', text)
        longest_word = ''
        for word in words:
            if word.endswith('e') and len(word) > len(longest_word):
                longest_word = word
        return longest_word

    def analyze_text(self):
        text = self.read_text()
        num_sentences = self.count_sentences(text)
        num_narrative, num_interrogative, num_imperative = self.count_sentence_types(text)
        avg_sentence_length = self.average_sentence_length(text)
        avg_word_length = self.average_word_length(text)
        num_smileys = self.count_smileys(text)
        capital_letters = self.find_all_capital_letters(text)
        replaced_text = self.replace_sequence(text)
        num_words_max_length = self.count_words_max_length(text)
        words_with_punctuation = self.find_words_with_punctuation(text)
        longest_word_with_e = self.find_longest_word_ending_with_e(text)

        # Сохраняем результаты анализа в файл
        with open(self.output_file, 'w', encoding='utf-8') as file:
            file.write(f"Number of sentences: {num_sentences}\n")
            file.write(f"Number of narrative sentences: {num_narrative}\n")
            file.write(f"Number of interrogative sentences: {num_interrogative}\n")
            file.write(f"Number of imperative sentences: {num_imperative}\n")
            file.write(f"Average sentence length: {avg_sentence_length}\n")
            file.write(f"Average word length: {avg_word_length}\n")
            file.write(f"Number of smileys: {num_smileys}\n")
            file.write(f"All capital letters: {capital_letters}\n")
            file.write(f"Replaced text: {replaced_text}\n")
            file.write(f"Number of words with max length: {num_words_max_length}\n")
            file.write(f"Words with punctuation: {words_with_punctuation}\n")
            file.write(f"Longest word ending with 'e': {longest_word_with_e}\n")

        psw: bytes = bytes(1234)
        # Создаем архив с результатами
        with zipfile.ZipFile('analysis_results.zip', 'w') as zipf:
            zipf.write(self.output_file)
            zipf.setpassword(psw)
            zipf.extractall("Task2", None, psw)
            print(zipf.getinfo(self.output_file))
            zipf.printdir()




