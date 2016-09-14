from data_Reader import CSVDataReader
#from geo import geomapping
from langdist import langDist
from landdist import landDist
import unicodecsv as csv


if __name__ == "__main__":
        
        read_data = CSVDataReader()
        #langdist = langDist()
        landdist = landDist()
        

        data = read_data.FileReader('result.csv')
        
        #mapper = geomapping()
        #mapper.mapping(data[1], data[4])

        #langdist.dist(data[1])
        usa = landdist.reader('states.csv')
        germany = landdist.reader('germany.csv')
        uk = landdist.reader('uk.csv')
        france = landdist.reader('france.csv')
        spain = landdist.reader('spain.csv')
        canada = landdist.reader('canada.csv')
        russia = landdist.reader('russia.csv')
        print (landdist.dist(data[5], usa, germany, uk, france, spain, canada, russia))
