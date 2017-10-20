import pandas as pd


def cleanData(data):
    '''cleans up rent and size colums (splits it to new columns sizeValue, sizeUnit, rentValue, rentUnit'''
    data = data.drop('Unnamed: 0', 1)
    data['sizeValue'] = None
    data['sizeUnit'] = None
    data['rentValue'] = None
    data['rentUnit'] = None
    #loops trough the data
    for ix, row in data.iterrows():
        # print(row['type'])
        s = row['total_size'].strip().split(' ')
        s1 = float(s[0].replace(',', '.'))
        s2 = s[1]
        data.loc[ix, ['sizeValue']] = s1
        data.loc[ix, ['sizeUnit']] = s2
        r = row['rent'].strip().split(' ')
        # dont touch the ### number lenght    ▼ spaces in my numbers!!
        r1 = float(r[0].replace(',', '.').replace(' ', ''))
        r2 = r[1]
        data.loc[ix, ['rentValue']] = r1
        data.loc[ix, ['rentUnit']] = r2
    return data




