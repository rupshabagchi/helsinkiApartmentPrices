import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

#read the testdata and the shapefile into a pandas dataframe and a geopandas geodataframe
map = gpd.read_file('data/pkSeutu.shp')
#reads postinumero as an int, tat is a problem when comparing because it drops 00 from beginniing
info = pd.read_csv('data/testdata.csv',  dtype={'POSTI_ALUE':str})

#print data to check
#print(map.head(5))
#print(info.head(5))

#try plotting the testdata stright from the geopandas
#map.plot(column = 'HE_VAKIY')
#plt.show()

#remove that column to test the merging of pandas and geopandas
map = map.drop('HE_VAKIY', 1)

#merge with postinumero
map = map.merge(info, on='POSTI_ALUE')

#print merged, should be same as earlier map
#print(map.head(5))

#plot
map.plot(column = 'HE_VAKIY')
plt.show()

#TODO
#remove axsis
#add legend
#add title
#save as png
#configure how bins, colors etc are chsen
#draw municipal borders (use kunnat.shp for it
#handle postinumero with missing values