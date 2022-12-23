import pandas as pd

def main():
	stocks = pd.read_csv("dow_jones_index (2).csv")
	stocks["date"] = stocks["date"].astype(str)
	# Question 2a
	walmart = stocks[stocks["stock"] == "WMT"]
	walmart_volume = walmart["volume"].sum()
	total_volume = stocks["volume"].sum()
	walmart_percentage = walmart_volume / total_volume

	bank_of_america = stocks[stocks["stock"] == "BAC"]
	bank_of_america_volume = bank_of_america["volume"].sum()
	bank_of_america_percentage = bank_of_america_volume / total_volume

	cisco = stocks[stocks["stock"] == "CSCO"]
	cisco_volume = cisco["volume"].sum()
	cisco_percentage = cisco_volume / total_volume
	overall = (walmart_percentage + bank_of_america_percentage + cisco_percentage) * 100
	print("The percentage of traded volume for Walmart, Bank of America, and Cisco is", round(overall, 2))

	# Question 2b
	stocks_sorted = stocks[(stocks["date"] >= "2/04/2011") & (stocks["date"] <= "6/17/2011")]
	average_volume = stocks_sorted["volume"].mean()
	print("The average volume of stocks traded between 2/04/2011 and 6/17/2011 is", round(average_volume, 2))

	# Question 2c
	max_volume = stocks[stocks["volume"] == stocks["volume"].max()]
	print("The stock with the highest volume traded is ", max_volume["stock"])
if __name__ == "__main__":
	main()

