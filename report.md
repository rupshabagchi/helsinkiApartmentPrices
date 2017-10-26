Report:

Idea

The idea of our project was to scrape apartment data from vuokraovi.com and make a webpage with some general statistics as maps and plots of apartments in the Helsinki area as well as a simple linear model for  predicting the price of apartments with certain parameters. In addition to the scraped data, we used spatial data obtained from the spatial data database Raituli (https://avaa.tdata.fi/-/paituli-paikkatietopalvelu).

##Scraping




Spatial data

The data we obtained was the municipality borders (https://etsin.avointiede.fi/fi/dataset/urn-nbn-fi-csc-kata20170313154359453160) and  the postal code statistic database Paavo (http://www.stat.fi/tup/paavo/index.html) these was mostly used to get the spatial data that we joined to our scraped


The plots

We made 3 different maps. One for average price/m^2, one for average size, and one for average build year. The one for average size was a bit problematic, because most areas have apartments of size 20-60 but then there are areas with average size of more than 300m^2 which made the visualization kind of hard. We solved this problem by capping the size of the scale at 200m^2.

Additional to the maps we made scatter plots for price versus apartment size. This shows us an almost linear correlation for these two.  Other than that the difference comes mostly from the area. The scatter plots were made for the whole area, the municipalities separately and for each postal code with at least 3 data points separately.

The model

[insert info about model]

The web page
[insert code about web page]
