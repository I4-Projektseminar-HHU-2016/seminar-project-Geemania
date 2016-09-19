import unicodecsv as csv
import re
from collections import Counter, OrderedDict

#Takes a csv file and splits data into several lists that are returned 
class CSVDataReader():

    def __init__(self):
        return
    def FileReader(self, fileName):

        print ('reading file...')

        self.temp_id = []
        self.temp_datelist = []
        self.temp_time_of_day = []

        self.text_Data = {}
        self.lang_Data = {}

        self.unique_tweets = 0

        self.tweets_per_hour = {}
        self.coordinates = {}
        self.country = {}
        
    
        with open(fileName, 'rb') as data:
            reader = csv.reader(data, delimiter=";", lineterminator="\r\n", encoding='utf-8')
        
            # reading row for row 
            for row in reader:

                self.split_date = row[1].split() # Splitting Date and Time
                self.split_place = []
                self.regex = re.compile('^\d{18}$')
                self.coords = []

                if (self.regex.match(row[0]) and (row[0] not in self.temp_id)):
            
                    self.temp_id.append(row[0])
                    self.unique_tweets += 1
            
                    self.text_Data[row[0]] = row[2].lower()  # save text into dictionary[tweet_id]
                    self.lang_Data[row[0]] = row[3].lower()
                
                    self.new_time = self.split_date[1].split(':') # hours, min. und sec. 
                    self.temp_time_of_day.append(self.new_time[0]) # saving only hours

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
        
                        self.coordinates[row[0]] = self.coords

                    if ('NaN' not in row[5]):
                        self.country[row[0]] = row[5]
    
            self.tweets_per_hour = Counter(self.temp_time_of_day) # counting tweets per hour
            self.tweets_per_hour = OrderedDict(sorted(self.tweets_per_hour.items(), key=lambda t: t[0]))
            data.close()
        return [self.text_Data, self.lang_Data,self.tweets_per_hour, self.unique_tweets, self.coordinates, self.country]
