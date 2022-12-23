def getISBN(number):
    numlist = list(map(int, number))
    partone = (3*(numlist[1])) + (3*(numlist[3])) + (3*(numlist[5])) + (3*(numlist[7])) + (3*(numlist[9])) + ((3*(numlist[11])))
    parttwo = numlist[0] + numlist[2] + numlist[4] + numlist[6] + numlist[8] + numlist[10]
    checksum = (10 - (partone + parttwo)) % 10
    if checksum == 10:
        # replace checksum with 0 in case it equals 10
        checksum == 0
    numlist.append(checksum)
    finalnumber = "".join(map(str, numlist))
    print("The ISBN-13 number is: " + finalnumber)
def main():
    number = input("Enter the first 12 digits of an ISBN-13 as a string: ")
    if len(number) == 12 and number.isnumeric():
        getISBN(number)
    else:
        print("error")
if __name__ == "__main__":
    main()