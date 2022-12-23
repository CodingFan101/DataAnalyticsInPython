from pandas import Series, DataFrame
import pandas as pd
import wget
import numpy as np

def main():
   df = pd.read_csv("processed.cleveland.data", header = None)

   new_df = df.replace('?', np.nan)
   new_df.dropna()
   print(new_df)
   # Question 2b
   # filter for female patients who are more than 40 years old but less than 50 years old
   female_patients = new_df[(new_df[1] == 0) & ((new_df[0] > 40) & (new_df[0] < 50))]
   # how many female patients are diagnosed with more than 50% diameter narrowing?
   female_diameters = female_patients[(female_patients[13] > 0)]
   print("The amount of female patients who are more than 40 years old but less than 50 years old, and have more than 50% narrowing is", len(female_diameters))

   # Question 2c
   # what is the average serum cholestoral level for patients diagnosed with more than 50% diameter narrowing?
   more_than_fifty = new_df[(new_df[13] > 0)]
   average_cholestoral = more_than_fifty[4].mean()
   print("The average cholestoral level for patients with more than 50% diameter narrowing is", round(average_cholestoral, 2))

   # Question 2d
   male_patients = new_df[(new_df[1] == 1)]
   # filter for male patients who have below average cholestoral but more than 50% diameter narrowing
   males_below_average = male_patients[(male_patients[4] < average_cholestoral)]
   males_more_than_50 = males_below_average[males_below_average[13] > 0]
   print("The number of male patients who have below average cholestoral but more than 50% diameter narrowing is", len(males_more_than_50))

   

if __name__ == "__main__":
    main()
