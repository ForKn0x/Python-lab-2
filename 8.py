import numpy as np
import math
from prettytable import PrettyTable

def euler(fn, a, b, y, steps):
    # Table Layout
    table = PrettyTable(["x", "slope", "y"])
    table.align = "r"
    # Step size
    h = (b - a) / steps
    # Euler
    for i in range(steps):
        slope = fn(a, y)
        y = round(y + h * slope, 4)
        a = round(a + h, 4)
        table.add_row([a, slope, y])
    return table

def function(x, y):
    return np.round(x ** 2 + x, 4)

table = euler(function, a=0, b=2, y=1, steps=20)
print(table)