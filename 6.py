import numpy as np
def function(x):
    return np.sin(x)/np.exp(x)

intervalBegin = 0
intervalEnd = np.pi
iterations = 20

step = (intervalEnd - intervalBegin) / iterations
integral = 0.5 * (function(intervalBegin) + function(intervalEnd))

for i in range(iterations):
    integral += function(intervalBegin + step * i)
integral *= step
print("Integral is equal to: ", integral)