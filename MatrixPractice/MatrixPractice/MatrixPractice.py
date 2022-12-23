import numpy as np
def sumMajorDiagnol(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i][i]
    print("Sum of major diagnol is", sum)

def sumRow(m, columnIndex):
    sum = 0
    for i in range(len(m[0])):
        sum += m[columnIndex][i]
    print("Sum of row", columnIndex, "is", sum)
        

def sumColumn(m, columnIndex):
    sum = 0
    for i in range(len(m)):
        sum += m[i][columnIndex]
    print("Sum of column", columnIndex, "is", sum)

def main():
    data = np.array([[1.5, 2, 3, 4], 
                     [5.5, 6, 7, 8], 
                     [9.5, 1, 3, 1]])
    sumMajorDiagnol(data)
    for i in range(len(data)):
        sumRow(data, i)
    for i in range(len(data[0])):
        sumColumn(data, i)
if __name__ == "__main__":
    main()
