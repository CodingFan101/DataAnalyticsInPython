def sortedNumber(number):
    numlist = list(map(int, str(number)))
    numlist.sort()
    result = "".join(map(str, numlist))
    print(result)
def main():
    try:
        number = int(input("Enter an unsigned integer number: "))
        # Check if number is signed
        if number < 0:
            print("Number is signed. Only unsigned numbers are allowed.")
            exit()
        sortedNumber(number)
    except ValueError:
        print("error")
if __name__ == "__main__":
    main()
