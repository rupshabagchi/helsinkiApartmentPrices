Report:

# Idea

The idea of our project was to scrape apartment data from vuokraovi.com and make a webpage with some general statistics as maps and plots of apartments in the Helsinki area as well as a simple linear model for  predicting the price of apartments with certain parameters. In addition to the scraped data, we used spatial data obtained from the spatial data database Raituli (https://avaa.tdata.fi/-/paituli-paikkatietopalvelu).

## Scraping
Data was collected by scraping vuokaovi.com. The scraper we used was based on one made by Teemo Tebest for Yleisradio (https://github.com/Yleisradio/yle-uutiset/tree/master/vuokraovi-scraper). The scraper made by Teemo was few years old, and vuokraovi.com had changes, so we had to mostly write our own, using Teemos scraper as a backbone. The scraped data was stored in mongoDB, where it could be easily accessed later.

## Data wrangling
Our scraper collected all listed rent apartments on vuokraovi.com, so once we had the database we cleaned the data:
All aparments whose renter was Forenom, since Forenom rents apartments for short time use, so the monthly rent is a lot higher that for normal apartments.
Vuokraovi.com was build so that we couldn't select the postal code areas we wanted in scraping phase, so we had to create a subset which only had apartments from Helsinki region
There were also three storage spaces in our data, which we removed.
Some outliers were also deleted, for example apartment with building year 1400 and a house with rent of 25 000€ per month. In the data there were also apartments that had some wrong data listed in the web page, for example one apartment had rent of 123456€ per month.


## Spatial data

The data we obtained was the municipality borders (https://etsin.avointiede.fi/fi/dataset/urn-nbn-fi-csc-kata20170313154359453160) and  the postal code statistic database Paavo (http://www.stat.fi/tup/paavo/index.html) these was mostly used to get the spatial data that we joined to our scraped


### The plots

We made 3 different maps. One for average price/m^2, one for average size, and one for average build year. The one for average size was a bit problematic, because most areas have apartments of size 20-60 but then there are areas with average size of more than 300m^2 which made the visualization kind of hard. We solved this problem by capping the size of the scale at 200m^2.

Additional to the maps we made scatter plots for price versus apartment size. This shows us an almost linear correlation for these two.  Other than that the difference comes mostly from the area. The scatter plots were made for the whole area, the municipalities separately and for each postal code with at least 3 data points separately.

## The model
The goal of the model was to predict rent of an apartment, given some parameters about the apartment. We chose to make a linear model. The model was built by studying the data, and selecting variables that had considerable effect on the rent. To be able to do this exploration all string-type variables had to be changed into dummy variables, for example "yksiö", "kaksio", "3 huonetta", "4 huonetta", "5+" were changed into factors 1, 2, 3, 4, 5, since R cannot fit linear model using strings.  
Some parameters were not used, since we didn't have sufficient data to use them for modeling, for example under 10 of the 2000 apartments in our dataset allowed pets, so it could not be used in predicting the rent. Some other parameters were not included, since analysis showed that they don't have significant (p > 0.05) effect in the amount of rent.
In the end we selected to use only the size and condition of the apartment as parameters, since they were the ones with clearest effect. Number of rooms could have been selected also, but it had the same effect on the price as the size of the apartment, since apartment that is yksiö also has small area. Because of this "number of rooms" parameter is just inaccurate version of "total size" parameter, so it was not used. 
Postal code was not included, since for some postal areas we only had under three datapoints, so building model that uses postal codes, would have required some quite sophisticated methods that we didn't have time for. Also it should be noted that inside Helsinki region postal code doesn't have very big effect on the rent.

## The web page
[insert code about web page]
