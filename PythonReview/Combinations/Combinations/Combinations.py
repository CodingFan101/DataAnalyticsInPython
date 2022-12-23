from itertools import combinations
def getcombinations(A, size):
    count = 0
    s = combinations(A, size)
    for i in s:
        count += 1
        print(i)
    print(count)

def main():
    A = []
    size = 10
    print("Enter 10 integers: ")
    for i in range(0, 10, 1):
        x = int(input())
        A.append(x)
    print(A)
    getcombinations(A, 2)

if __name__ == "__main__":
    main()


