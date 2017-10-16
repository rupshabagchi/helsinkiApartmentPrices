import pandas as pd

def grouper(data, groupedBy, calculateFrom):
    '''groups the dataframe data by the given column and gives the mean of the columns with names in given list
    assumes the dataframe data contains the column names groupedBy, and all in the calculate from. Returns mean for
    each group'''

    groupedStat = pd.DataFrame()
    #grouping data by months (and years)
    grouped = data.groupby(groupedBy)
    #looping trough the groups and calculating means. doing this for bpoth the dataframes that the excersise wanted
    for key, group in grouped:
        #caunting mean
        calculatedRow = group[calculateFrom].mean()
        #caunting std
        #todo check how to give new column name in this step to be able to get columns like
        #todo  columnA_mean columnA_std etc this needed for multiple stats for working
        #calculatedRow = group[calculateFrom].std()

        #defining key
        calculatedRow[groupedBy] = key
        #appending the mean of the month
        groupedStat = groupedStat.append(calculatedRow, ignore_index=True)
    return groupedStat



# testcode for the grouper
#data = data = pd.read_csv('grouperTest.txt', sep = '\s+', skiprows=[1], na_values=[-9999])
#data['MONTH'] = data['DATE'].astype(str).str.slice(start = 4, stop = 6).astype(int)
#calculateFromthese =['PRCP', 'TAVG', 'TMAX', 'TMIN']
#groupBy = 'MONTH'
#means = grouper(data, groupedBy= groupBy, calculateFrom=calculateFromthese)
#print(means.head(5))