from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def main():
    df = pd.read_csv("dow_jones_index.csv")
    
    # remove the dollar signs from the "close" column
    df["close"] = df["close"].str.replace("$", "", regex = True)
    # convert the "close" column to a float
    df["close"] = df["close"].astype(float)
    
    # Question 1 - Find the stock info for Walmart
    walmart_data = df[df["stock"] == "WMT"]
    print(walmart_data)

    # Question 2 - Find stock info for the maximum volume stock traded by Walmart
    print(walmart_data[walmart_data["volume"] == walmart_data["volume"].max()])

    # Question 3 - Find Stock information for the minimum opening priced stock traded among all companies
    print(df[df["open"] == df["open"].min()])

    # Question 4 - Find average closing price for Walmart
    print("The average closing price for Walmart is", round(walmart_data["close"].mean(), 2))
    
if __name__ == "__main__":
    main()
