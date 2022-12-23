import pandas as pd

def main():
	names = pd.read_csv("baby-names.csv")
	
	# convert the gender and name columns to a string
	names['gender'] = names['gender'].astype(str)
	names['name'] = names['name'].astype(str)
	# Question 1a
	boys_1900 = names[(names['gender'] == "boy") & (names['year'] == 1900)]
	# to find the most common name, use the 'percent' column
	most_common_boy_name = boys_1900[(boys_1900['percent'] == boys_1900['percent'].max())]
	print("Question 1a:", most_common_boy_name['name'])

	# Question 1b
	girls_1900 = names[(names['gender'] == "girl") & (names['year'] == 1900)]
	most_common_girl_name_1900 = girls_1900[(girls_1900['percent'] == girls_1900['percent'].max())]
	print("Question 1b (Part 1):", most_common_girl_name_1900['name'])
	
	girls_2000 = names[(names['gender'] == "girl") & (names['year'] == 2000)]
	most_common_girl_name_2000 = girls_2000[(girls_2000['percent'] == girls_2000['percent'].max())]
	print("Question 1b (Part 2):", most_common_girl_name_2000['name'])
	
	# Question 1c
	# print the top 5 names of girls who were born in 2000
	# get the top 5 names in girls_2000
	girl_names_sorted = girls_2000.sort_values(by = 'percent', ascending=False)
	print("Question 1c:", girl_names_sorted['name'][0:5])

	print("Question 1d:")
	# Question 1d
	unique_years = names['year'].unique()
	for year in unique_years:
		ratio_dict = {}
		boys = names[(names['year'] == year) & (names['gender'] == "boy")]
		girls = names[(names['year'] == year) & (names['gender'] == "girl")]
		boys_ratio = boys['percent'].sum()
		girls_ratio = girls['percent'].sum()
		boys_to_girls = boys_ratio / girls_ratio
		ratio_dict[year] = boys_to_girls
		print(ratio_dict)
		
	
	
if __name__ == "__main__":
	main()

