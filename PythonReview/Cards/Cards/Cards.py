from itertools import combinations

def main():
    allcombos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    s = combinations(allcombos, 4)
    count = 0
    for i in s:
        if sum(i) == 24:
            count += 1
    print(count)
if __name__ == "__main__":
    main()

