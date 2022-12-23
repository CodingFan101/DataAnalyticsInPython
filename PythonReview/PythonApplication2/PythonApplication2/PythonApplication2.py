def sumDigits(number):
    sum = 0
    digit = 0
    while(number > 0):
        digit = number % 10
        sum += digit
        number = number // 10
    print("The sum of the digits is: " + str(sum))

def main():
    number = int(input("Enter a number: "))
    sumDigits(number)

if __name__ == "__main__":
    main()