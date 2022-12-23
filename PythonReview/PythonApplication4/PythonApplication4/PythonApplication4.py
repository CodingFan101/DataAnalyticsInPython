def eliminateduplicates(numlist):
    newlist = []
    for i in numlist:
        if i not in newlist:
            newlist.append(i)
    print(newlist)

def main():
    n = int(input("Enter the list size: "))
    A = [0] * n
    for i in range(0, n, 1):
        number = 101
        while (number < 1 or number > 100):
            number = int(input("Enter a number from 1 to 100: "))
        A[i] = number
    print(A)
    eliminateduplicates(A)

if __name__ == "__main__":
    main()
