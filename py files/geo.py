import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class geomapping():
    def __init__(self):
        return

    def mapping(self, language, coordinates):

        self.fig = plt.figure(figsize=(18, 4), dpi=250)
        plt.title("Tweets zu #Legion #Warcraft und #WorldofWarcraft")

        map = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180, lat_ts=20, resolution='l')
        map.bluemarble(scale=0.3)

        plt.ion()
        plt.show()

        for elem in coordinates:
            self.x, self.y = map(coordinates[elem][0], coordinates[elem][1])
            if language[elem] == 'en':
                map.plot(self.x, self.y, 'ro', markersize=3)
            elif language[elem] == 'de':
                map.plot(self.x, self.y, 'go', markersize=3)
            elif language[elem] == 'fr':
                map.plot(self.x, self.y, 'bo', markersize=3)
            elif language[elem] == 'es':
                map.plot(self.x, self.y, 'yo', markersize=3)
            elif language[elem] == 'und':
                map.plot(self.x, self.y, 'wo', markersize=3)
            plt.draw()
    
        plt.ioff()
        plt.show()
        return
