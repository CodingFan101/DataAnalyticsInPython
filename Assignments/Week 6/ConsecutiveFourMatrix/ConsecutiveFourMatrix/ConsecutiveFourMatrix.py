import numpy as np

def isConsecutiveFour(m):
    status = False
    # check rows
    for i in range(len(m)):
        for j in range(len(m[i]) - 3):
            if m[i][j] == m[i][j + 1] == m[i][j + 2] == m[i][j + 3]:
                print("True")
                status = True
    # check columns
    for i in range(len(m) - 3):
        for j in range(len(m[i])):
            if m[i][j] == m[i + 1][j] == m[i + 2][j] == m[i + 3][j]:
                print("True")
                status = True
    # check diagonals
    for i in range(len(m) - 3):
        for j in range(len(m[i]) - 3):
            if m[i][j] == m[i + 1][j + 1] == m[i + 2][j + 2] == m[i + 3][j + 3]:
                print("True")
                status = True
    for i in range(len(m) - 3):
        for j in range(len(m[i]) - 3):
            if m[i][j + 3] == m[i + 1][j + 2] == m[i + 2][j + 1] == m[i + 3][j]:
                print("True")
                status = True
    if status == False:
        print("False")
         
def main():
    try:
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))
        if (rows < 4) and (columns < 4):
            print("We cannot proceed with these dimensions")
            exit()
        matrix = np.zeros((rows, columns), dtype = int)
        for i in range(rows):
            for j in range(columns):
                matrix[i][j] = int(input("Enter a number: "))
        print(matrix)
        isConsecutiveFour(matrix)
    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()
