def isConsecutiveFour(numlist):
    consecutivelist = []
    for i in range(0, len(numlist) - 1, 1):
        if numlist[i] == numlist[i + 1]:
            consecutivelist.append(i)
    size = len(consecutivelist) + 1
    if(size < 4):
        print("There are not four consecutive numbers with the same value.")
    elif(size == 4):
        print("There are four consecutive numbers with the same value.")
    else:
        print("There are more than four consecutive numbers with the same value.")

def main():
    n = 0
    while(n < 4):
        n = int(input("Enter the list size: "))
    A = [0] * n
    for i in range(0, n, 1):
        number = 101
        while (number < 1 or number > 100):
            number = int(input("Enter a number from 1 to 100: "))
        A[i] = number
    print(A)
    isConsecutiveFour(A)

if __name__ == "__main__":
    main()
