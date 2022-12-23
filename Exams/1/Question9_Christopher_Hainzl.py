def commonDigits(num1, num2):
    number1 = str(num1)
    number2 = str(num2)
    commonnumbers = []
    for i in number1:
        if i in number2:
            if i not in commonnumbers:
                commonnumbers.append(i)
    for number in commonnumbers:
        print(number)

def main():
    try:
        num1, num2 = input("Enter two integers: ").split(", ")
        firstnumber = int(num1)
        secondnumber = int(num2)
        if(firstnumber < 0) or (secondnumber < 0):
            # Checks if numbers are signed
            print("Signed number(s) detected")
            exit()
        commonDigits(num1, num2)
    except ValueError:
        print("You must enter a number!")
if __name__ == "__main__":
    main()