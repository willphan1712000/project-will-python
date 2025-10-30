from numpy.typing import NDArray
import willphanpy
from collections import Counter
from tqdm import tqdm as progress
import numpy as np

__all__ = [
    "Count"
]

class Count:
    '''
    aka Bag of Words technique
    - For a word in a sentence, count how many times it appears in the sentence
    - The main goal is to generate a dataset with format
    --------------------------------------------------------------------------------------
    -             vocab1  vocab2 vocab3 ...
    - Sample 1
    - Sample 2
    - Sample 3
    - ...
    --------------------------------------------------------------------------------------
    - Vocabulary is also known as feature in the dataset
    '''

    def __init__(self, corpus: list[str] = []):
        self.__corpus = np.array(corpus) # store corpus
        self.__dictionary: dict[str, int] = {} # store vocabulary in dictionary
        self.__vocabulary: list[str] = [] # vocabulary list - features
        self.__count: list[Counter] = [] # count for entire corpus
        self.__vector: NDArray = None # vector for entire corpus

        self.__tp = willphanpy.TextPreprocessing() # Text preprocessing from willphanpy library

    def makeCount(self):
        '''
        Perform count operation
        '''
        for doc in progress(self.__corpus, desc="Vectorize the corpus"):
            self.__tp.text = doc
            self.__tp.preprocess()

            # add NEW vocab to the vocabulary dictionary
            for token in self.__tp.tokens:
                self.__dictionary[token] = 0

            # add counter for current doc tokens to count
            count = Counter(self.__tp.tokens)
            self.__count.append(count)

        # make vocab list based on dictionary
        self.__vocabulary = list(self.__dictionary.keys())

        # dictionary that maps each vocab to its index
        vocab_index = {word: i for i, word in enumerate(self.__vocabulary)}

        # make vector list based on dictionary + count, this is the dataset with desired format
        self.__vector = np.zeros((len(self.__count), len(self.__vocabulary)), dtype=int)
        for row, count in enumerate(progress(self.__count, desc="Making vector list")):
            for word, number in count.items():
                self.__vector[row, vocab_index[word]] = number

    def getCorpus(self):
        '''
        Retrive corpus
        '''
        return self.__corpus

    def getVector(self):
        'Retrive vectorized words in numpy array format'
        return self.__vector

    def getVocabulary(self):
        'Retrive vocabulary list - features'
        return self.__vocabulary

    def getCount(self):
        'Retrive dictionary of count'
        return self.__count

    def getDictionary(self):
        '''
        Retrive vocabulary in dictionary
        '''
        return self.__dictionary