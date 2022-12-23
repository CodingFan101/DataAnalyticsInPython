def deviation(x):
    sum = 0
    devsum = 0
    for i in range(0, len(x), 1):
        sum += x[i]
    mean = sum / len(x)
    for i in range(0, len(x), 1):
        devsum += ((x[i]) - mean) ** 2
    deviation = (devsum / (len(x) - 1)) ** 0.5
    print("Standard deviation: " + str(deviation))

def mean(x):
    sum = 0
    for i in range(0, len(x), 1):
        sum += x[i]
    mean = sum / len(x)
    print("Mean: " + str(mean))

def main():
    n = int(input("Enter the list size: "))
    A = [0] * n
    for i in range(0, n, 1):
        number = 101
        while (number < 1 or number > 100):
            number = float(input("Enter a number from 1 to 100: "))
        A[i] = number
    print(A)
    mean(A)
    deviation(A)

if __name__ == "__main__":
    main()

