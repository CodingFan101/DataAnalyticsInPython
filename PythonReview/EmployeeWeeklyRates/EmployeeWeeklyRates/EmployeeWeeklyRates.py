import numpy as np

def main():
    employee = np.array([[2, 4, 3, 4, 5, 8, 8],
                         [7, 3, 4, 3, 3, 4, 4],
                         [3, 3, 4, 3, 3, 2, 2],
                         [9, 3, 4, 7, 3, 4, 1],
                         [3, 5, 4, 3, 6, 3, 8],
                         [3, 4, 4, 6, 3, 4, 4],
                         [3, 7, 4, 8, 3, 8, 4],
                         [6, 3, 5, 9, 2, 7, 9]])
    # declare an empty dictionary named employee_rates
    employee_rates = {}
    for i in range(len(employee)):
        # store the row index and the sum of each row as a key-value pair in employee_rates
        employee_rates[i] = sum(employee[i])
    # sort the dictionary by the values in descending order
    employee_rates = sorted(employee_rates.items(), key=lambda x: x[1], reverse=True)
    print(employee_rates)

if __name__ == "__main__":
    main()
