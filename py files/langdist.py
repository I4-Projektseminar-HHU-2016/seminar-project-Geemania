import matplotlib as plt
import nltk
from nltk import FreqDist

class langDist(object):
    def __init__(self):
        return

    def dist(self, data):

        self.langs = []
        
        for value in data.values():
            self.langs.append(value)

        self.freq = FreqDist(self.langs).most_common()
        
        return self.freq
