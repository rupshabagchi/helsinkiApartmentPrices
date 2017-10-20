import pandas as pd
import dataCleaner as clean
import matplotlib.pyplot as plt
import os

myfolder = "figures/scatter"

groupedBy = 'postal_code'
filename = 'data/apartments.csv'

data = pd.read_csv(filename, dtype = {'postal_code':str} )
data = clean.cleanData(data)

#plots scatterplot of price versus size of whole area
data.plot.scatter( y = 'rentValue', x = 'sizeValue')
plt.xlabel('size of apartment')
plt.ylabel('price of apartment')
plt.savefig(myfolder + '/priceVersusSizeScatterAll.png')

groupedStat = pd.DataFrame()
#grouping data by months (and years)
grouped = data.groupby(groupedBy)

#looping trough the groups and calculating means. doing this for bpoth the dataframes that the excersise wanted
for key, group in grouped:
    total_rows = len(group.axes[0])
    #plotting scatterplot for each postal code with at least 3 datapoints
    if (total_rows > 2):
        group.plot.scatter(y='rentValue', x='sizeValue')
        title = "Price versus size in postal code area: " + key
        plt.xlabel('size of apartment m^2')
        plt.ylabel('price of apartment €/kk')
        plt.title(title)
        filename = "priceVersusSizeScatter" + key +".png"
        filepath = os.path.join(myfolder, filename)
        plt.savefig(filepath)

