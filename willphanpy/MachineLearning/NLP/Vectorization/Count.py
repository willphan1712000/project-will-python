from willphanpy.MachineLearning.NLP.TextPreProcessing.TextPreprocessing import TextPreprocessing
from collections import Counter

class Count:
    '''
    aka Bag of Words technique
    - For a word in a sentence, count how many times it appears in the sentence
    '''

    def __init__(self, text: str = ""):
        self.text = text
        self.vocabulary = []
        self.__tp = TextPreprocessing()

    def count(self):
        self.__tp.text = self.text
        self.__tp.preprocess()
        print(Counter(self.__tp.tokens))