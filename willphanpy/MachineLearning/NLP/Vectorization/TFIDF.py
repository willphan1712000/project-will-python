import numpy as np
from collections import Counter
from willphanpy.MachineLearning.NLP.TextPreProcessing.TextPreprocessing import TextPreprocessing
from tqdm import tqdm

__all__ = [
    "TFIDF"
]

def progress_bar_generation(corpus, desc):
    '''
    Method to generate progress bar
    '''
    def document_generator(data):
        for doc in data:
            yield doc

    doc_gen = document_generator(corpus)

    progress_bar = tqdm(doc_gen, total=len(corpus), desc= desc)

    return progress_bar

class TFIDF():
    '''
    Term Frequency - Inverse Document Frequency
    - TF: compute by how many times a word appears in a sentence divided by the total number of words in that sentence, determining how common the word is in the context of the sentence
    - IDF: compute by log( number of documents in a corpus divided by how many documents that have a word, determining how common the word is across all documents
    - TF-IDF score is a statistical measure that reflects the importance or relevance of a term (word) in a specific document relative to a large collection of documents (the corpus).
    - TF-IDF is built on top of Bag of Word technique
    '''

    def __init__(self):
        self.__corpus = []
        self.__dictionary: dict[str, int] = {}
        self.__vocabulary: list[str] = []

        self.__tf_vector = []

        self.__idf_vector = []

        self.__tfidf = []

        self.__tf_count: list[Counter] = [] # count for entire corpus

    def fit(self, corpus: list[str] = []):
        self.__corpus = progress_bar_generation(corpus, desc="Vectoring the corpus")
        self.__computeTF()

    def __computeTF(self):
        '''
        Compute TF score for each word in the vocabulary
        '''
        tp = TextPreprocessing()

        for doc in self.__corpus:
            tp.text = doc
            tp.preprocess()

            # add NEW vocab to the vocabulary dictionary
            for token in tp.tokens:
                self.__dictionary[token] = 0

            # add counter for current doc tokens to count
            count = Counter(tp.tokens)
            total = sum(count.values())

            self.__tf_count.append({ key : val / total for key, val in count.items()} )

        # make vocab list based on dictionary
        self.__vocabulary = list(self.__dictionary.keys())

        # dictionary that maps each vocab to its index
        vocab_index = {word: i for i, word in enumerate(self.__vocabulary)}

        # make vector list based on dictionary + count, this is the dataset with float64 format
        self.__tf_vector = np.zeros((len(self.__tf_count), len(self.__vocabulary)), dtype=np.float64)
        for row, count in enumerate(self.__tf_count):
            for word, number in count.items():
                self.__tf_vector[row, vocab_index[word]] = number

        
    def __computeIDF(self):
        '''
        Compute IDF score for each word in the vocabulary
        - use natural log for IDF score
        '''
        pass

    def __computeTFIDF(self):
        '''
        Compute TF-IDF score by element-wise multiplying TF vector and IDF vector
        '''
        pass

    def getCorpus(self):
        '''
        Retrieve corpus
        '''
        return self.__corpus

    def getTFVector(self):
        return self.__tf_vector

            
            
        