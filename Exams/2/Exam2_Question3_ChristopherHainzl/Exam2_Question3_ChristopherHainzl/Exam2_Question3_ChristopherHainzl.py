from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np

def main():
    df = pd.read_csv("flag.data", header = None)
    # Question 3b
    red = df[df[10] == 1]
    green = df[df[11] == 1]
    blue = df[df[12] == 1]
    gold = df[df[13] == 1]
    white = df[df[14] == 1]
    black = df[df[15] == 1]
    orange = df[df[16] == 1]
    # rank all the dataframes based on their length
    num_of_reds = len(red)
    num_of_greens = len(green)
    num_of_blues = len(blue)
    num_of_golds = len(gold)
    num_of_whites = len(white)
    num_of_blacks = len(black)
    num_of_oranges = len(orange)
    # store all of this in a dataframe
    colors = DataFrame({'Colors': ['Red', 'Green', 'Blue', 'Gold', 'White', 'Black', 'Orange'],
                        'Flag Amounts / Rankings': [num_of_reds, num_of_greens, num_of_blues, num_of_golds, num_of_whites, num_of_blacks, num_of_oranges]})
    print(colors)
    # rank the dataframe based on the number of flags
    colors = colors.rank(method = 'max', ascending = False)
    # restore the columns
    colors['Colors'] = ['Red', 'Green', 'Blue', 'Gold', 'White', 'Black', 'Orange']
    # print the dataframe
    print(colors)

    # Question 3c
    # list the amount of countries which have animated images in their flag
    animated_images = df[df[26] == 1]
    print("The amount of countries which have animated images in their flag is", len(animated_images))

    # Question 3d
    # list the top three countries in Asia based on their size
    asian_countries = df[df[1] == 5]
    # arrange the Asian countries in descending order based on their size
    asian_countries_sorted = asian_countries.sort_values(by = 3, ascending = False)
    # print the top three countries in Asia based on their size
    print("The top three countries in Asia based on their size are")
    print()
    print(asian_countries_sorted[0][0:3])
if __name__ == "__main__":
    main()
