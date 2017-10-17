import geopandas as gpd
import pandas as pd
import mapMaker
import matplotlib.pyplot as plt

'''tests the makeMap method'''

#read the testdata and the shapefile into a pandas dataframe and a geopandas geodataframe
map = gpd.read_file('data/pkSeutu.shp')
#reads postinumero as an int, tat is a problem when comparing because it drops 00 from beginniing
info = pd.read_csv('data/testdata.csv',  dtype={'POSTI_ALUE':str})

mapMaker.makeMap(map, info, 'POSTI_ALUE', 'HE_VAKIY', 'Helsinki väkiluku')

