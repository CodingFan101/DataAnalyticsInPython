from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np
def main():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
    filename = wget.download(url)
    df = pd.read_csv(filename)
    df.columns = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 
                  'body-style', 'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 
                  'curb-weight', 'engine-type', 'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 
                  'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
    df = df.replace('?', np.nan)
    # drop all the rows in the datafram with na values
    df.dropna()
    df['price'] = pd.to_numeric(df['price'])
    df['highway-mpg'] = pd.to_numeric(df['highway-mpg'])
    print()
    
    # find most expensive make
    most_expensive_make = df.iloc[df['price'].idxmax()]['make']
    print("The most expensive make is: ", most_expensive_make)

    # find least expensive make
    least_expensive_make = df.iloc[df['price'].idxmin()]['make']
    print("The least expensive make is: ", least_expensive_make)
    # find most expensive sedan, print the entire row
    sedan = df.loc[(df['body-style'] == 'sedan')]
    most_expensive_sedan = sedan.loc[sedan['price'].idxmax()]['make']
    print("The most expensive sedan is: " + most_expensive_sedan)
    # find sedan with maximum highway-mpg
    sedan_with_max_highway_mpg = sedan.loc[sedan['highway-mpg'].idxmax()]['make']
    print("The sedan with the most highway-mpg is: " + sedan_with_max_highway_mpg)
    
    print()
    # calculate average highway-mpg for all sedans
    avg_highway_mpg = sedan['highway-mpg'].mean()
    # calculate average price for all sedans
    avg_price_sedan = sedan['price'].mean()
    # find all the sedans that have more than the average highway-mpg but less than the average price
    new_sedans = sedan.loc[(sedan['highway-mpg'] > avg_highway_mpg) & (sedan['price'] < avg_price_sedan)]['make']
    print("Here are all the sedans that have more than the average highway-mpg but below the average price: ")
    print(new_sedans)
if __name__ == "__main__":
    main()
