import nltk
from nltk import FreqDist
from bokeh.charts import Donut, show, output_file

class langDist(object):
    def __init__(self):
        return

    def dist(self, data):

        self.langs = []
        self.names = []
        self.values= []
        self.dumpV = []
        self.v = 0
        self.dicts = {}
        
        for value in data.values():
            self.langs.append(value)

        self.freq = FreqDist(self.langs).most_common()
        for elem in self.freq:
            (self.key, self.val) = elem
            if self.val < 500: #write to rest
                self.dumpV.append(self.val)
            else:
                self.names.append(self.key+': '+str(self.val))
                self.values.append(self.val)

        for dump in self.dumpV:
            self.v += dump

        self.names.append('rest: '+str(self.v)) #dictionaries
        self.values.append(self.v)
        
        self.dicts['labels'] = self.names
        self.dicts['vals'] = self.values

        self.graph = Donut(self.dicts, values='vals', label='labels', title='Language Frequency Distribution') #draw donut with bokeh
        output_file("language_distribution.html")
        show(self.graph)
        
        return
