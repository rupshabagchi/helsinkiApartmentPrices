import geopandas as gpd
import pandas as pd
import mapMaker
import matplotlib.pyplot as plt
import dataCleaner as clean
import grouper
import os

'''draws a lot of maps'''
mapfile = 'data/shapefiles/pkSeutu.shp'
datafile = 'data/formatted_full_data.csv'

#read the scraped data and clean it
data = pd.read_csv(datafile, dtype = {'postal_code':str} )
data = clean.cleanData(data)
#needed to be same as in shapefile
data['POSTI_ALUE'] = data['postal_code']
data['pricePerSquare'] = data['rentValue'] / data['sizeValue']

#read the testdata and the shapefile into a pandas dataframe and a geopandas geodataframe
map = gpd.read_file(mapfile)
map['POSTI_ALUE'] = map['POSTI_ALUE']

#group the data by postal code and colculate mean size value
data =  grouper.grouper(data, groupedBy= 'POSTI_ALUE', calculateFrom=['sizeValue', 'rentValue', 'pricePerSquare', 'built_year'])
data['POSTI_ALUE'] = data['POSTI_ALUE']

#will toss runtime warning, because more than 20 figures opened
#draw maps per postal code

folder = 'figures/averageYearMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgBuiltYear' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'built_year', 'Average built year', \
                     filepath,  spesArea = alue, spesCol = 'POSTI_ALUE',)
folder = 'figures/averagePriceMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgPricePerSquare' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'pricePerSquare', 'Average price per square in €/m^2',\
                 filepath, spesArea = alue, spesCol = 'POSTI_ALUE')

folder = 'figures/averageSizeMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgSize' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'sizeValue', 'Average size of apartment in m^2',\
                 filepath, spesArea = alue, spesCol = 'POSTI_ALUE', maxValue = 250)


mapMaker.makeMap(map, data, 'POSTI_ALUE', 'built_year', 'Average built year' , "figures/averageBuiltYearMap.png")
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'sizeValue', 'Average size of apartment in m^2','figures/averageApartmentSize.png', maxValue = 200)
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'pricePerSquare', 'Average price per square in €/m^2', 'figures/averagePriceSquareMap.png')

