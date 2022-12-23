from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np
def main():
    # read the breast cancer data into a dataframe
    df = pd.read_csv('wdbc.data', header = None)
    
    # filter for malignant tumors
    malignant = df[df[1] == 'M']

    #filter for benign tumors
    benign = df[df[1] == 'B']

    # Question 1
    # get the number of patients with malignant tumors
    print("The number of patients with malignant tumors is " + str(len(malignant)))
    
    # get the number of patients with benign tumors
    print("The number of patients with benign tumors is " + str(len(benign)))

    # Question 2
    # get the average radius of malignant tumors
    average_malignant = malignant[2].mean()
    print("The average radius of malignant tumors is " + str(round(average_malignant, 2)))

    # Question 3
    # find the number of patients that have a radius greater than average_malignant but have a benign tumor
    benign_filtered = benign.loc[(benign[2] > average_malignant)]
    print("The number of patients that have a radius greater than average_malignant but have a benign tumor is " + str(len(benign_filtered)))
    

    # Question 4
    # get the maximum tumor radius of malignant tumors
    print("The maximum tumor radius of malignant tumors is " + str(malignant[2].max()))

    # get the maximum tumor radius of benign tumors
    print("The maximum tumor radius of benign tumors is " + str(benign[2].max()))

    # Question 5
    # get the minimum tumor radius of malignant tumors
    print("The minimum tumor radius of malignant tumors is " + str(malignant[2].min()))

    # get the minimum tumor radius of benign tumors
    print("The minimum tumor radius of benign tumors is " + str(benign[2].min()))
if __name__ == "__main__":
    main()
