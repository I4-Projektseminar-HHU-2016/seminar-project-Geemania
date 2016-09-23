import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from os import path

class geomapping():
    def __init__(self):
        return

    def mapping(self, language, coordinates):

		self.path = path.join(path.dirname(__file__), 'geomap.png') #define path for result picture

		self.fig = plt.figure(figsize=(18, 4), dpi=150) #basemap figure details
		plt.title("Tweets zu #Legion #Warcraft und #WorldofWarcraft") #sets the title for the results

		m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180,urcrnrlon=180, lat_ts=20, resolution='l') #basemap default settings
		m.etopo(scale=0.3) #basemap style

		plt.ion()
		plt.show()
        
		for elem in coordinates: #marking geo tags on map with language color
			self.x, self.y = m(coordinates[elem][0], coordinates[elem][1])
			if language[elem] == 'en':
				m.plot(self.x, self.y, 'ro', markersize=4) #red for english
			elif language[elem] == 'en-gb':
				m.plot(self.x, self.y, 'ro', markersize=4) #red for english
			elif language[elem] == 'de':
				m.plot(self.x, self.y, 'go', markersize=4) #green for german
			elif language[elem] == 'fr':
				m.plot(self.x, self.y, 'bo', markersize=4) #blue for french
			elif language[elem] == 'es':
				m.plot(self.x, self.y, 'yo', markersize=4) #yellow for spanish
			elif language[elem] == 'ru':
				m.plot(self.x, self.y, 'co', markersize=4) #cyan for russian
			elif language[elem] == 'it':
				m.plot(self.x, self.y, 'mo', markersize=4) #magenta for italian
			elif language[elem] == 'und':
				m.plot(self.x, self.y, 'wo', markersize=4) #white for undefined
			plt.draw()
    
		plt.ioff()
		plt.show()
		self.fig.savefig(self.path, transparent=True, bbox_inches='tight') #saving result to geomap.png
		return
		plt.close()
