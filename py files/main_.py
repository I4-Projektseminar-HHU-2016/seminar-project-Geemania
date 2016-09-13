from data_Reader import CSVDataReader
from geo import geomapping


if __name__ == "__main__":
        
        read_data = CSVDataReader()

        data = read_data.FileReader('result.csv')
        
        mapper = geomapping()
        mapper.mapping(data[1], data[4])

		

