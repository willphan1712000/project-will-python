import willphanpy
from collections import Counter
from tqdm import tqdm as progress

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
        self.__corpus: list[str] = corpus # store corpus
        self.__dictionary: dict(str, int) = {} # store vocabulary in dictionary
        self.__vocabulary: list[str] = [] # vocabulary list - features
        self.__count: list[dict(str, int)] = [] # count for entire corpus
        self.__vector: list[list[int]] = [] # vector for entire corpus

        self.__tp = willphanpy.TextPreprocessing()

    def makeCount(self):
        '''
        Perform count operation
        '''
        for doc in progress(self.__corpus, desc="Vectorize the corpus"):
            self.__tp.text = doc
            self.__tp.preprocess()
            vector = []

            # add NEW vocab to the vocabulary dictionary
            for token in self.__tp.tokens:
                self.__dictionary[token] = 0

            # add counter for current doc tokens to count
            count = Counter(self.__tp.tokens)
            self.__count.append(count)

        # make vocab list based on dictionary
        for key in progress(self.__dictionary, desc="Making vocabulary list"):
            self.__vocabulary.append(key)

        # make vector list based on dictionary + count
        for count in progress(self.__count, desc="Making vector list"):
            vector = []
            for key in self.__dictionary:
                if key in count:
                    vector.append(count[key])
                else:
                    vector.append(0)

            self.__vector.append(vector)


    def getCorpus(self):
        '''
        Retrive corpus
        '''
        return self.__corpus

    def getVector(self):
        'Retrive vectorized words'
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