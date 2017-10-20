import pandas as pd
import dataCleaner as clean

data = pd.read_csv('/home/shiera/courses/IntroductionToDataScience/projec/helsinkiApartmentPrices/scraper/apartment.csv')
data = clean.cleanData(data)

print(data.head(5))

