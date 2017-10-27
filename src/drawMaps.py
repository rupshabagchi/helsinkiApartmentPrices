import geopandas as gpd
import pandas as pd
import mapMaker
import matplotlib.pyplot as plt
import dataCleaner as clean
import grouper
import os

'''Code for drawing all the maps! 
uses methods grouper and mapMaker'''

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

#data.to_csv('/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/data/averages.csv')

#will toss runtime warning, because more than 20 figures opened
#draw maps per postal code
'''
folder = 'webpage/src/images/averageYearMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgBuiltYear' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'built_year', ' Average Construction Year', \
                     filepath,  spesArea = alue, spesCol = 'POSTI_ALUE',)
    print('poastalcode ' + alue + ' for average year')                 

folder = 'webpage/src/images/averagePriceMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgPricePerSquare' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'pricePerSquare', 'Average Price per Square Meter in €',\
                 filepath, spesArea = alue, spesCol = 'POSTI_ALUE')
    print('poastalcode ' + alue + ' average price')              

folder = 'webpage/src/images/averageSizeMap'
for ix, row in map.iterrows():
    alue = row['POSTI_ALUE']
    name = 'avgSize' + alue + '.png'
    filepath = os.path.join(folder, name)
    mapMaker.makeMap(map, data, 'POSTI_ALUE', 'sizeValue', 'Average size of apartment in m^2',\
                 filepath, spesArea = alue, spesCol = 'POSTI_ALUE', maxValue = 250)
    print('poastalcode ' + alue + ' for average size')              

'''
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'built_year', ' Average Construction Year' , "webpage/src/images/averageBuiltYearMap.png")
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'sizeValue', 'Average size of apartment in m^2','webpage/src/images/averageApartmentSize.png', maxValue = 200)
mapMaker.makeMap(map, data, 'POSTI_ALUE', 'pricePerSquare', 'Average Price per Square Meter in €', 'webpage/src/images/averagePriceSquareMap.png')

