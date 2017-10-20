import geopandas as gpd
import pandas as pd
import mapMaker
import matplotlib.pyplot as plt
import dataCleaner as clean
import grouper

'''tests the makeMap method'''
#read the scraped data and clean it
data = pd.read_csv('scraper/apartment.csv')
data = clean.cleanData(data)
#needed to be same as in shapefile
data['POSTI_ALUE'] = data['postal_code']
data['pricePerSquare'] = data['rentValue'] / data['sizeValue']

#read the testdata and the shapefile into a pandas dataframe and a geopandas geodataframe
map = gpd.read_file('data/pkSeutu.shp')
map['POSTI_ALUE'] = map['POSTI_ALUE'].astype(int).astype(str)

#group the data by postal code and colculate mean size value
data =  grouper.grouper(data, groupedBy= 'POSTI_ALUE', calculateFrom=['sizeValue', 'rentValue', 'pricePerSquare'])
data['POSTI_ALUE'] = data['POSTI_ALUE'].astype(int).astype(str)




#draw map
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'sizeValue', 'Average apartmentSize', 'figures/averageApartmentSize.png')
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'pricePerSquare', 'Average price per square in €/m^2', 'figures/averagePriceSquareMap.png')

