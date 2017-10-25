import pandas as pd
import dataCleaner as clean
import matplotlib.pyplot as plt
import os

myfolder = 'figures/scatter'

groupedBy = 'POSTI_ALUE'
filename = 'data/formatted_full_data.csv'
kuntaFilename = 'data/pkSeutu.csv'

data = pd.read_csv(filename, dtype = {'postal_code':str} )
data = clean.cleanData(data)
kuntaArvot = pd.read_csv(kuntaFilename, dtype = {'POSTI_ALUE':str, 'KUNTA':str})
data['POSTI_ALUE'] = data['postal_code']
data = data.ix[data['sizeValue'] <= 500]

#making a kunta column to the data
data['KUNTA'] = None
for ix, row in data.iterrows():
    alue = row['POSTI_ALUE']
    kunta = kuntaArvot[kuntaArvot['POSTI_ALUE'] == alue]['KUNTA'].item()
    data.loc[ix, 'KUNTA'] = kunta

kunnittain = data.groupby('KUNTA')

#making plot for whole area with all 'kunta' with different color
fig, ax = plt.subplots(1, 1)
colors = ['red', 'green', 'blue', 'black']
i = 0
kuntaNames = ['Espoo', 'Helsinki', 'Vantaa', 'Kauniainen']
for key,group in kunnittain:
    group.plot.scatter(y='rentValue', x='sizeValue', ax = ax, color = colors[i])
    i +=1
plt.legend(kuntaNames)
plt.title('scatterplot of prices versus size in Helsinki area')
plt.xlabel('size of apartment')
plt.ylabel('price of apartment')
plt.savefig(myfolder + '/priceVersusSizeScatterAll.png')
plt.cla()
plt.clf()

#plotting each kunta separetly
fig, ax = plt.subplots(1, 1)
i = 0
kuntaNames = ['Espoo', 'Helsinki', 'Vantaa', 'Kauniainen']
for key,group in kunnittain:
    group.plot.scatter(y='rentValue', x='sizeValue', ax = ax, color = 'black', alpha = 0.5)
    #plt.legend(kuntaNames)
    plt.title('scatterplot of prices versus size in ' + kuntaNames[i])
    plt.xlabel('size of apartment')
    plt.ylabel('price of apartment')
    filename = myfolder + '/pricaVersusSizeScatter' + kuntaNames[i] + '.png'
    plt.savefig(filename)
    plt.cla()
    plt.clf()
    i +=1


#plotting each postal code
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

