def main():
	# read in the text file
	file = open("random_integers.txt", "r")
	# store all the numbers in the file in a list, with a space as the separator
	numbers = file.read().split()
	# close the file
	file.close()
	# Question 3a
	print("The number of entries in this list is", len(numbers))
	# Question 3b
	# find and print distinct numbers and their frequencies in the list
	countednumbers = []
	for i in range(len(numbers)):
		if numbers[i] not in countednumbers:
			print(numbers[i], "appears", numbers.count(numbers[i]), "times")
			countednumbers.append(numbers[i])
		else:
			continue
	# Question 3c
	# convert all the elements to integers using the map function
	numbers = list(map(int, numbers))
	# display all the numbers in reverse order
	print("The numbers in reverse order are", numbers[::-1])
			
	
if __name__ == "__main__":
	main()

