import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

def _grupeGeoframeToFrame(geoData, data, groupColumnName):
    '''takes a geodataframe and an dataframe and groups them with the column with the name groupColumnName
    removes all other dublicate named columns from the geodataframe before merging, to keep the same names'''

    # getting keys (coulumn names) from both frames
    mapKeys = list(geoData.keys())
    infoKeys = list(data.keys())

    # looping trough the keys and removing dublicates
    for key in mapKeys:
        if key in infoKeys:
            if key != groupColumnName:
                geoData = geoData.drop(key, 1)

    # merge with the given column
    return geoData.merge(data, on=groupColumnName)


def makeMap(map, info, mergeColumn, drawColumn, title, savePath = None, maxValue = None, spesArea = None, spesCol = None):
    '''takes a geodataframe 'map' and a dataframe 'info' merges them by column by name mergeColumn
     and plots he map with the data from drawColumn
     if savepath is not given the map is printed, othervise it is saved
     assumes map has olumn "KUNTA"'''

    #for plotting kunta borders and empty values
    kunnat = map.dissolve(by='KUNTA')
    basemap = map

    # merge the dataframe info to the geodataframe map
    map = _grupeGeoframeToFrame(map, info, groupColumnName=mergeColumn)


    # for making colorbar see the max and min values of the data we want to plot
    #if max axe value is given use that instead
    colorbarMin = map[drawColumn].min()
    if (maxValue == None):
        colorbarMax = map[drawColumn].max()
    else:
        colorbarMax = maxValue

    #needed for plotting multiple in a map
    fig, ax = plt.subplots(1, 1)

    #plot
    #plot empty on the bottom
    basemap.plot(color = '#D3D3D3', ax = ax, edgecolor = 'grey')

    #plot the map
    plottedMap = map.plot(edgecolor = 'grey', column = drawColumn, cmap = 'YlGnBu', vmin = colorbarMin, vmax = colorbarMax, ax = ax, alpha = 1)
    # get the map as a figure

    #plot borders
    kunnat.plot(ax = ax, alpha = 0, edgecolor = 'black')


    if (spesArea != None and spesCol != None):
        ar = basemap[basemap[spesCol].str.contains(spesArea)]

        ar.plot(ax=ax, alpha=0, edgecolor='red')


    #remove x and y axis from the map
    plottedMap.set_axis_off()

    #put the title to the map
    fig.suptitle(title)
    #some internet workaround for making the colorbar for geopandas (from matplotlib, geopandas doesent have its own yet
    sm = plt.cm.ScalarMappable(cmap='YlGnBu', norm=plt.Normalize(vmin= colorbarMin, vmax=colorbarMax))
    # fake up the array of the scalar mappable. Urgh...
    sm._A = []
    fig.colorbar(sm)



    if (savePath == None):
        plt.show()
    else:
        plt.savefig(savePath)

    plt.cla()
    plt.clf()
    #TODO

    #add unit to legend


