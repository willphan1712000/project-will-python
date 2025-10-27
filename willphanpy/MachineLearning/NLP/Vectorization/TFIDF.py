import numpy as np

from tqdm import tqdm as progress
from collections import Counter
from willphanpy.MachineLearning.NLP.TextPreProcessing.TextPreprocessing import TextPreprocessing

__all__ = [
    "TFIDF"
]

class TFIDF:
    '''
    Term Frequency - Inverse Document Frequency
    - TF: compute by how many times a word appears in a sentence divided by the total number of words in that sentence, determining how common the word is in the context of the sentence
    - IDF: compute by log( number of documents in a corpus divided by how many documents that have a word, determining how common the word is across all documents
    - TF-IDF score is a statistical measure that reflects the importance or relevance of a term (word) in a specific document relative to a large collection of documents (the corpus).
    '''

    def __init__(self, corpus: list[str] = []):
        self.corpus: list[str] = corpus
        self.__tp_list: list[TextPreprocessing] = []
        self.vocabulary: dict[str, float]= {}

        self.tf_list = []
        self.tf_vector = []

        self.idf_list = []
        self.idf_vector = []

        self.score = []

        self.__getVocabulary()

    def __getVocabulary(self):
        '''
        Extract vocabulary from the corpus after text preprocessing
        - Each document in corpus has its own text preprocessing object
        '''
        for doc in self.corpus:
            tp = TextPreprocessing(doc)
            tp.preprocess()

            self.__tp_list.append( tp )
            for token in tp.tokens:
                self.vocabulary[token] = 0

    def computeTF(self) -> list[dict]:
        '''
        Computer TF score for each word in the vocabulary
        '''

        for tp in progress(self.__tp_list, desc="TF in progress"):
            temp = self.vocabulary.copy()
            vector = []

            counter = Counter(tp.tokens)
            for key in counter:
                temp[key] = counter[key] / len(tp.tokens)

            self.tf_list.append(temp)

            for key in temp:
                vector.append(temp[key])

            self.tf_vector.append(vector)

    def computeIDF(self):
        '''
        Compute IDF score for each word in the vocabulary
        - use natural log for IDF score
        '''

        for tp in progress(self.__tp_list, desc="IDF in progress"):
            temp = self.vocabulary.copy()
            vector = []

            for token in tp.tokens:
                count = 0
                
                for tp in self.__tp_list:
                    if token in tp.tokens:
                        count += 1

                temp[token] = np.log( len(self.corpus) / count )
                
            self.idf_list.append(temp)

            for key in temp:
                vector.append(temp[key])

            self.idf_vector.append(vector)

    def computeTFIDF(self):
        '''
        Compute TF-IDF score by element-wise multiplying TF vector and IDF vector
        '''
        self.score = np.multiply(
            np.array(self.tf_vector),
            np.array(self.idf_vector)
        )

            

            
            
        