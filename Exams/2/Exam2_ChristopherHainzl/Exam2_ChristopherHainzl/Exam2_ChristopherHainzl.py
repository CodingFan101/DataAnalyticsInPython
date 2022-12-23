from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np

def main():
    # Question 1
    df = pd.read_csv("adult.data", header = None)
    # drop missing values
    df = df.replace("?", np.nan)
    df.dropna()
    print(df)

    # Question 1b
    # count the number of people who make over 50k a year
    over_50k = df[df[14] == " >50K"]
    print("Number of people who make over 50k a year: ", len(over_50k))

    # Question 1c
    # find the education level of the majority of the population who makes more than 50k a year
    print("Education level of the majority of the population who makes more than 50k a year: ", over_50k[3].value_counts().idxmax())

    # Question 1d
    # find the country with the lowest number of people who make more than 50k a year
    print("Country with the lowest number of people who make more than 50k a year: ", over_50k[13].value_counts().idxmin())

if __name__ == "__main__":
    main()
