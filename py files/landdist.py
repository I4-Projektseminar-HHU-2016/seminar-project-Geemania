import unicodecsv as csv
import nltk
from nltk import FreqDist
from bokeh.charts import Bar, show, output_file
from bokeh.charts.attributes import CatAttr

class landDist(object):
    def __init__(self):
        return

    def reader(self, fileName):
        self.states_list = []
        with open(fileName, 'rb') as data:
            self.csvreader = csv.reader(data, delimiter=",", lineterminator="\r\n", encoding='utf-8')
            for row in self.csvreader:
                self.states_list.append(row)

        data.close()
        return self.states_list

    def dist(self, data, states, germany, uk, france, spain, canada, russia):

        print ('Tweets with location: ', len(data))
        self.countries = [states, germany, uk, france, spain, canada, russia]
        self.names = ['USA', 'Germany', 'UK', 'France', 'Spain', 'Canada', 'Russia']
        
        self.azeroth = ['Azeroth', 'Stormwind', 'Dalaran', 'Lordaeron', 'Azeroth', 'World of Warcraft',
                        'Draenor', 'Undercity', 'Deathguard', "Val'sharah", 'Frostfire Ridge', 'Lordearon',
                        'Blizzard Entertainment', 'Dun Modr', 'Darnassus', 'Warcraft', 'Emerald Dream',
                        "Quel'Dorei", 'Teldrassil', 'Cenarion Circle', 'Orgrimmar', 'The Nexus', 'Uldum']
                        
        self.leftover = ['Sweden', 'Denmark', 'Norway', 'Finland', 'Argentina', 'Australia']
        self.country_list = []

        self.values = []
        self.label = []
        self.dicts = {}
        
        self.index = 0
        for country in self.countries:
            for state in country:
                for elem in state:
                    self.keys = []
                    self.tmp = elem.rstrip()
                    for entry in data:
                        if data[entry].find(self.tmp) != -1:
                            self.country_list.append(self.names[self.index])
                            self.keys.append(entry)
                    
                    for key in self.keys:
                        if key in data:
                            data.pop(key, None)
        
            self.index += 1

        for wow in self.azeroth:
            self.keys = []
            for entry in data:
                if data[entry].find(wow) != -1:
                    self.country_list.append('World of Warcraft')
                    self.keys.append(entry)

            for key in self.keys:
                        if key in data:
                            data.pop(key, None)

        for left in self.leftover:
            self.keys = []
            for entry in data:
                if data[entry].find(left) != -1:
                    self.country_list.append(left)
                    self.keys.append(entry)
                elif data[entry] == 'Россия':
                    self.country_list.append('Russia')
                    self.keys.append(entry)
                elif data[entry] == 'UK':
                    self.country_list.append('UK')
                    self.keys.append(entry)
                elif data[entry] == 'United Kingdom':
                    self.country_list.append('UK')
                    self.keys.append(entry)
                elif data[entry].find('Wales') != -1:
                    self.country_list.append('UK')
                    self.keys.append(entry)

            for key in self.keys:
                if key in data:
                    data.pop(key, None)

        self.test = []
        for elem in data:
            self.test.append(data[elem])
        self.freq_Rest = FreqDist(self.test).most_common()
        with open('rest.csv', 'ab') as resultFile:
            writer = csv.writer(resultFile, delimiter=";", lineterminator="\r\n", encoding='utf-8')
            for elem in self.freq_Rest:
                writer.writerow(elem)

        self.rest = []
        for elem in data:
            self.country_list.append('The rest combined')
            self.rest.append(elem)
        for rest in self.rest:
                if rest in data:
                    data.pop(rest, None)

        print ('undefined Tweets: ', len(data))
        
        self.freq = FreqDist(self.country_list).most_common()

        for elem in self.freq:
            (self.key, self.val) = elem
            self.label.append(self.key)
            self.values.append(self.val)

        self.dicts['labels'] = self.label
        self.dicts['vals'] = self.values

        self.graph = Bar(self.dicts, label=CatAttr(columns=['labels'], sort=False), values='vals', color='navy', title='Country Frequency Distribution', legend=False)
        output_file("country_distribution.html")
        show(self.graph)
        
        return
