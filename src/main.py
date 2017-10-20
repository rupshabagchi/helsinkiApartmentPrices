import pandas as pd
import dataCleaner as clean
import matplotlib.pyplot as plt
import geopandas as gpd
import mapMaker


filename = 'data/apartments.csv'
data = pd.read_csv(filename)
data = clean.cleanData(data)

#plots scatterplot of price versus size
data.plot.scatter( y = 'rentValue', x = 'sizeValue')
plt.xlabel('size of apartment')
plt.ylabel('price of apartment')
plt.savefig('figures/priceVersusSize.png')