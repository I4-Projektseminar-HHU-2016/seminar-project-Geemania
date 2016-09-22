from langdetect import detect
from nltk import FreqDist
from bokeh.charts import Donut, show, output_file

class langDetectDist(object):
    def __init__(self):
        return

    def dist(self, data):

        self.langs = []
        self.names = []
        self.values= []
        self.dumpV = []
        self.v = 0
        self.dicts = {}
        
        for value in data.values():	#parse tweets and try to detect the language via langdected and name the language
            try:
                self.langs.append(detect(value))
            except:
                self.langs.append('undetected') #if detection fails name it undetected

        self.freq = FreqDist(self.langs).most_common() #frequency of languages and sort it
        for elem in self.freq: #parse entries and write language and frequency value
            (self.key, self.val) = elem
            if self.val < 500: #write to rest
                self.dumpV.append(self.val)
            else:
                self.names.append(self.key+': '+str(self.val)) #write to dict for graph
                self.values.append(self.val)

        for dump in self.dumpV:
            self.v += dump

        self.names.append('rest: '+str(self.v)) #dictionaries for bokeh
        self.values.append(self.v)
        
        self.dicts['labels'] = self.names
        self.dicts['vals'] = self.values

        self.graph = Donut(self.dicts, values='vals', label='labels', title='Langdetect Frequency Distribution') #draw donut with bokeh
        output_file("langdetect_distribution.html")
        show(self.graph)
        
        return
