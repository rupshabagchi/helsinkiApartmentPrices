import pandas as pd
import dataCleaner as clean
import matplotlib.pyplot as plt
import os

'''draws the scatterplots for the data. For some reason the relative path does not work
please change the path before using '''

myfolder = '/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/webpage/src/images/scatter'
filename = '/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/data/formatted_full_data.csv'
kuntaFilename = '/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/data/pkSeutu.csv'

groupedBy = 'POSTI_ALUE'
data = pd.read_csv(filename, dtype = {'postal_code':str} )
data = clean.cleanData(data)
kuntaArvot = pd.read_csv(kuntaFilename, dtype = {'POSTI_ALUE':str, 'KUNTA':str})
data['POSTI_ALUE'] = data['postal_code']
data = data.ix[data['sizeValue'] <= 500]


#making a kunta column to the data ad name of postal code
data['KUNTA'] = None

for ix, row in data.iterrows():
    alue = row['POSTI_ALUE']
    kunta = kuntaArvot[kuntaArvot['POSTI_ALUE'] == alue]['KUNTA'].item()
    data.loc[ix, 'KUNTA'] = kunta

kunnittain = data.groupby('KUNTA')

#making plot for whole area with all 'kunta' with different color
fig, ax = plt.subplots(1, 1, subplot_kw={'xlim': (0,500), 'ylim': (0, 8000)})
colors = ['red', 'green', 'blue', 'yellow']
i = 0
kuntaNames = ['Espoo', 'Helsinki', 'Vantaa', 'Kauniainen']
for key,group in kunnittain:
    group.plot.scatter(y='rentValue', x='sizeValue', ax = ax, color = colors[i], alpha = 0.5)
    i +=1
plt.legend(kuntaNames)
plt.title('scatterplot of prices versus size in Helsinki area', fontsize = 19)
plt.xlabel('size of apartment m^2')
plt.ylabel('price of apartment €/mo')
plt.savefig(myfolder + '/priceVersusSizeScatterAll.png')
plt.cla()
plt.clf()

#plotting each kunta separetly

i = 0
kuntaNames = ['Espoo', 'Helsinki', 'Vantaa', 'Kauniainen']
for key,group in kunnittain:
    fig, ax = plt.subplots(1, 1, subplot_kw={'xlim': (0,500), 'ylim': (0, 8000)})
    group.plot.scatter(y='rentValue', x='sizeValue', ax = ax, color = 'black', alpha = 0.5)
    #plt.legend(kuntaNames)
    plt.xlabel('size of apartment m^2')
    plt.ylabel('price of apartment €/mo')

    filename = myfolder + '/pricaVersusSizeScatter' + kuntaNames[i] + '.png'
    plt.savefig(filename)
    i +=1
    plt.cla()
    plt.clf()


#plotting each postal code
#grouping data by months (and years)
grouped = data.groupby(groupedBy)

#looping trough each postal code
for key, group in grouped:
    nimi = kuntaArvot[kuntaArvot['POSTI_ALUE'] == key]['NIMI'].item()
    namn = kuntaArvot[kuntaArvot['POSTI_ALUE'] == key]['NAMN'].item()
    total_rows = len(group.axes[0])
    #plotting scatterplot for each postal code with at least 3 datapoints
    if (total_rows > 2):
        fig, ax = plt.subplots(1, 1, subplot_kw={'xlim': (0, 500), 'ylim': (0, 8000)})
        group.plot.scatter(y='rentValue', x='sizeValue')
        title = "Price versus size in postal code area: " + key + "\n" + nimi + "\n" + namn
        plt.subplots_adjust(top=0.8)
        plt.xlabel('size of apartment m^2')
        plt.ylabel('price of apartment €/mo')
        plt.title(title, fontsize = 19)
        filename = "priceVersusSizeScatter" + key +".png"
        filepath = os.path.join(myfolder, filename)
        plt.savefig(filepath)
        plt.cla()
        plt.clf()

