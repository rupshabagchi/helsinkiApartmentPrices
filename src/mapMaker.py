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


def makeMap(map, info, mergeColumn, drawColumn):
    '''takes a geodataframe 'map' and a dataframe 'info' merges them by column by name mergeColumn
     and plots he map with the data from drawColumn'''

    #merge the dataframe info to the geodataframe map
    _grupeGeoframeToFrame(map, info, groupColumnName=mergeColumn)

    #plot
    map.plot(column = drawColumn)
    plt.show()

    #TODO
    #remove axsis
    #add legend
    #add title
    #save as png
    #configure how bins, colors etc are chsen
    #draw municipal borders (use kunnat.shp for it
    #handle postinumero with missing values


