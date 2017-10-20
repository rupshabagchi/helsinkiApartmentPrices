import pandas as pd
import dataCleaner as clean
import matplotlib.pyplot as plt
import geopandas as gpd
import mapMaker


data = pd.read_csv('/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/scraper/apartment.csv')
data = clean.cleanData(data)

#plots scatterplot of price versus size
data.plot.scatter( x = 'rentValue', y = 'sizeValue')

plt.show()