def occurrences(numlist, size):
    count = [0] * 101
    for i in range(0, size, 1):
        idx = numlist[i]
        count[idx] = count[idx] + 1
    for i in range(0, 101, 1):
        if count[i] > 0:
            print(str(i) + " occurs " + str(count[i]) + " time(s).")

def main():
    n = int(input("Enter the list size: "))
    A = [0] * n
    for i in range(0, n, 1):
        number = 101
        while (number < 1 or number > 100):
            number = int(input("Enter a number from 1 to 100: "))
        A[i] = number
    print(A)
    occurrences(A, n)

if __name__ == "__main__":
    main()
