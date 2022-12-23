def countOccurrences(string):
    countedcharacters = []
    for char in string:
        if char not in countedcharacters:
            print(char, "occurs", string.count(char), "time(s)")
            countedcharacters.append(char)
        else:
            continue
    print()


def main():
    string = input("Enter a string: ")
    if string.isalpha():
        countOccurrences(string.lower())
    else:
        print("Error")
        exit()

if __name__ == "__main__":
    main()
