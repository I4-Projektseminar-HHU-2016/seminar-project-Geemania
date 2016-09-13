from data_Reader import CSVDataReader
from geo import geomapping
from langdist import langDist


if __name__ == "__main__":
        
        read_data = CSVDataReader()
        langdist = langDist()

        data = read_data.FileReader('result.csv')
        
        mapper = geomapping()
        mapper.mapping(data[1], data[4])

        langdist.dist(data[1])
