def isPalindrome(string):
    if string[::] == string[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
    
def main():
    string = input("Enter a string: ")
    if string.isalpha():
        isPalindrome(string.lower())
    else:
        print("Error")

if __name__ == "__main__":
    main()
