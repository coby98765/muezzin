import re


class Cleaner:
    @staticmethod
    def run(text):
        print("Processor Run.")
        clean = Cleaner.clean_text(text)
        word_count = Cleaner.word_count(clean)
        return clean,word_count

    @staticmethod
    def clean_text(text:str):
        # remove symbols
        clean_str = re.sub(r'[^A-Za-z0-9 ]+', "", text)
        # to lower
        lower_str = clean_str.lower()
        return lower_str

    @staticmethod
    def word_count(text:str):
        list_text = text.split(" ")
        return len(list_text)