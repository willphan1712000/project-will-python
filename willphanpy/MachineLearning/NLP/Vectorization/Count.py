from willphanpy.MachineLearning.NLP.TextPreProcessing.TextPreprocessing import TextPreprocessing
from collections import Counter

__all__ = [
    "Count"
]

class Count:
    '''
    aka Bag of Words technique
    - For a word in a sentence, count how many times it appears in the sentence
    '''

    def __init__(self, text: str = ""):
        self.text = text
        self.vocabulary = []
        self.count = None

        self.__tp = TextPreprocessing()

    def makeCount(self):
        self.__tp.text = self.text
        self.__tp.preprocess()
        self.vocabulary = self.__tp.tokens
        self.count = Counter(self.vocabulary)