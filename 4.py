import numpy as np
import math
from prettytable import PrettyTable

def difference_table(x, y, return_delta=False):
    # Table Definitions:
    n = len(x)
    dTable = np.zeros((n, n))
    dTable[:, 0] = y
    # Table Layout:
    column_names = ["Y", "△1", "△2", "△3", "△4", "△5", "△6", "△7", "△8", "△9", "△10"]
    table = PrettyTable(column_names)
    table.align = "r"
    # Generating Forward Difference Table
    for i in range(1, n):
        for j in range(0, n - i):
            dTable[j][i] = round(dTable[j + 1][i - 1] - dTable[j][i - 1], 4)
    # Output Structure
    num_columns = min(dTable.shape[1], 11)
    for row in dTable:
        row = row[:num_columns].copy()
        row.resize((11))
        table.add_row(row)
    # Returns
    if not return_delta:
        return table
    elif return_delta == "forward":
        # Returns n Forward Deltas, default=5
        n = min(dTable.shape[1], 5 + 1)
        return dTable[0, 1:n]
    elif return_delta == "backward":
        # Returns n Backward Deltas, default=5
        n = min(dTable.shape[1], 6)
        j = 1
        del_Y = []
    for i in range(dTable.shape[0] - 1, dTable.shape[0] - n, -1):
        del_Y.append(dTable[i - 1, j])
        j += 1
    return del_Y

def forward_interop(x_pred):
    # Data:
    x = np.array([0.20, 0.22, 0.24, 0.26, 0.28, 0.30])
    y = np.array([1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139])
    # Calculating h and p:
    h = x[1] - x[0]
    p = (x_pred - x[0]) / h
    # Forward Differences From Table:
    del_Y = difference_table(x, y, return_delta="forward")
    # Forward Interpolation Polynomial (upto △ 5)
    y_pred = (
    y[0]
    + del_Y[0] * p
    + del_Y[1] * p * (p - 1) / math.factorial(2)
    + del_Y[2] * p * (p - 1) * (p - 2) / math.factorial(3)
    + del_Y[3] * p * (p - 1) * (p - 2) * (p - 3) / math.factorial(4)
    + del_Y[4] * p * (p - 1) * (p - 2) * (p - 3) * (p - 4) / math.factorial(5)
    )
    return y_pred

print("====Forward====")
print(f"f(0.21) = {forward_interop(0.21)}")
print(f"f(0.29) = {forward_interop(0.29)}")

def backward_interop(x_pred):
    # Data:
    x = np.array([0.20, 0.22, 0.24, 0.26, 0.28, 0.30])
    y = np.array([1.6596, 1.6698, 1.6804, 1.6912, 1.7024, 1.7139])
    # Calculating h and p:
    h = x[1] - x[0]
    p = (x_pred - x[-1]) / h
    # Backward Differences From Table:
    del_Y = difference_table(x, y, return_delta="backward")
    # Forward Interpolation Polynomial (upto △ 5)
    y_pred = (
    y[-1]
    + del_Y[0] * p
    + del_Y[1] * p * (p + 1) / math.factorial(2)
    + del_Y[2] * p * (p + 1) * (p + 2) / math.factorial(3)
    + del_Y[3] * p * (p + 1) * (p + 2) * (p + 3) / math.factorial(4)
    + del_Y[4] * p * (p + 1) * (p + 2) * (p + 3) * (p + 4) / math.factorial(5)
    )
    return y_pred

print("====Backward====")
print(f"f(0.21) = {backward_interop(0.21)}")
print(f"f(0.29) = {backward_interop(0.29)}")