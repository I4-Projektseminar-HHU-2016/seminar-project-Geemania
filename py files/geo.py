import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

class geomapping():
    def __init__(self):
        return

    def mapping(self, language, coordinates):

        self.fig = plt.figure(figsize=(12, 6), dpi=200)
        plt.title("Tweets zu #Legion #Warcraft und #WorldofWarcraft")

        m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180, lat_ts=20, resolution='c')
        m.etopo(scale=0.2)

        plt.ion()
        plt.show()

        for elem in coordinates:
            self.x, self.y = m(coordinates[elem][0], coordinates[elem][1])
            if language[elem] == 'en':
                m.plot(self.x, self.y, 'ro', markersize=3)
            elif language[elem] == 'de':
                m.plot(self.x, self.y, 'go', markersize=3)
            elif language[elem] == 'fr':
                m.plot(self.x, self.y, 'bo', markersize=3)
            elif language[elem] == 'es':
                m.plot(self.x, self.y, 'yo', markersize=3)
            elif language[elem] == 'und':
                m.plot(self.x, self.y, 'wo', markersize=3)
            plt.draw()
    
        plt.ioff()
        plt.show()
        return
