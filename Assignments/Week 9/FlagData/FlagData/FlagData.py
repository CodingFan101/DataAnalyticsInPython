from pandas import Series, DataFrame
import pandas as pd
import wget

def main():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/flags/flag.data'
    filename = wget.download(url)
    df = pd.read_csv(filename)
    colnames = ['name', 'landmass', 'zone', 'area', 'population', 'language', 'religion', 'bars', 'stripes', 'colours', 'red', 'green', 'blue', 'gold', 'white', 'black', 'orange', 'mainhue', 'circles', 'crosses', 'saltires', 'quarters', 'sunstars', 'crescent', 'triangle', 'icon', 'animate', 'text', 'topleft', 'botright']
    df.columns = colnames
    print()
    na_countries = df.loc[(df['landmass'] == 1), 'population'].idxmax()
    print("The country with the largest population in North America is: " + df.loc[na_countries, 'name'])
    asian_countries = df.loc[(df['landmass'] == 5), 'population'].idxmax()
    print("The country with the largest population in Asia is: " + df.loc[asian_countries, 'name'])
    african_countries = df.loc[(df['landmass'] == 4), 'area'].idxmax()
    print("The largest country in Africa is: " + df.loc[african_countries, 'name'])
    oceania_countries = df.loc[(df['landmass'] == 6)]
    # group oceania_countries by how many times each religion occurs in the dataframe
    oceania_religion = oceania_countries.groupby('religion').size()
    # get the index of the largest value in the series
    largest_religion = oceania_religion.idxmax()
    print("The most common religion in Oceania is: " + str(largest_religion))
    
if __name__ == "__main__":
    main()
