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
    geoData = geoData.merge(data, on=groupColumnName)


def makeMap(map, info, mergeColumn, drawColumn, title, savePath = None):
    '''takes a geodataframe 'map' and a dataframe 'info' merges them by column by name mergeColumn
     and plots he map with the data from drawColumn
     if savepath is not given the map is printed, othervise it is saved'''

    #merge the dataframe info to the geodataframe map
    _grupeGeoframeToFrame(map, info, groupColumnName=mergeColumn)

    # for making colorbar see the max and min values of the data we want to plot
    colorbarMin = map[drawColumn].min()
    colorbarMax = map[drawColumn].max()

    #plot
    plottedMap = map.plot(column = drawColumn, cmap = 'Blues', vmin = colorbarMin, vmax = colorbarMax)

    # get the map as a figure
    fig = plottedMap.get_figure()

    #remove x and y axis from the map
    plottedMap.set_axis_off()

    #put the title to the map
    fig.suptitle(title)

    #some internet workaround for making the colorbar for geopandas (from matplotlib, geopandas doesent have its own yet
    sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin= colorbarMin, vmax=colorbarMax))
    # fake up the array of the scalar mappable. Urgh...
    sm._A = []
    fig.colorbar(sm)

    if (savePath == None):
        plt.show()
    else:
        plt.savefig(savePath)

    #TODO
    #draw municipal borders (use kunnat.shp for it)
    #handle postinumero with missing values - is this needed?, how to handle
    #add unit to legend


