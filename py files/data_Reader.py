import unicodecsv as csv
import re
from collections import Counter, OrderedDict


class CSVDataReader():

        def __init__(self):
                return
        def FileReader(self, fileName):

                self.temp_id = []
                self.temp_datelist = []
                self.temp_time_of_day = []

                self.text_Data = {}
                self.lang_Data = {}

                self.unique_tweets = 0

                self.tweets_per_hour = {}
                self.coordinates = []
        
                
                with open(fileName, 'rb') as data:
                        reader = csv.reader(data, delimiter=";", lineterminator="\r\n", encoding='utf-8')
                        
                        # Die csv Datei wird Zeile fuer Zeile eingelesen und aufs Datum 
                        # geprueft um die relevanten Daten zu filtern
                        for row in reader:

                                self.split_date = row[1].split() # Trennung von Datum und Uhrzeit
                                self.split_place = []
                                self.regex = re.compile('^\d{18}$')
                                self.coords = []

                                if (self.regex.match(row[0]) and (row[0] not in self.temp_id)):
                                        
                                        self.temp_id.append(row[0])
                                        self.unique_tweets += 1
                                        
                                        self.text_Data[row[0]] = row[2].lower()  # save text into dictionary[tweet_id]
                                        self.lang_Data[row[0]] = row[3].lower()
                                
                                        self.new_time = self.split_date[1].split(':') # Stunden, Min. und Sek. aufbrechen
                                        self.temp_time_of_day.append(self.new_time[0]) # Nur Stunden gespeichert

                                        if ('NaN' not in row[4]):
                                                
                                                self.temp = row[4].replace('[[[', '')
                                                self.temp = self.temp.replace(']]]', '')
                                                self.temp = self.temp.replace('[', '')
                                                self.temp = self.temp.replace(']', '')
                                                self.temp = self.temp.replace(' ', '')

                                                self.temp_coords = self.temp.split(',')
                                                
                                                self.temp_lat = (float(self.temp_coords[0])+float(self.temp_coords[4])) /2
                                                self.temp_lat = round(self.temp_lat, 6)
                                                self.temp_long = (float(self.temp_coords[1])+float(self.temp_coords[5])) /2
                                                self.temp_long = round(self.temp_long, 6)
                                                
                                                self.coords.append(self.temp_lat)
                                                self.coords.append(self.temp_long)
                                                
                                                self.coordinates.append(self.coords)
                                                
                        self.tweets_per_hour = Counter(self.temp_time_of_day) # Zaehlen der tweets je Stunde
                        self.tweets_per_hour = OrderedDict(sorted(self.tweets_per_hour.items(), key=lambda t: t[0]))
                        data.close()
                return [self.text_Data, self.lang_Data,self.tweets_per_hour, self.unique_tweets, self.coordinates]
                
########################################################################
#																	   #
#   Der Quellcode beider Dateien wurde in Zusammenarbeit mit Raphael   #
#   Katschke geschrieben 											   #
#																	   #
########################################################################
