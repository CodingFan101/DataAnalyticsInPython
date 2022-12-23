from itertools import combinations
def summationForm(number):
    for i in range(1, number):
        for j in combinations(range(1, number), i):
            if sum(j) == number:
                print(j)

def main():
    try:
        number = int(input("Enter a positive number less than 20: "))
        if number > 0 and number < 20:
            summationForm(number)
        else:
            print("Error")
    except ValueError:
        print("You must enter a number!")

if __name__ == "__main__":
    main()
