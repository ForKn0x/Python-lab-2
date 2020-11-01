import numpy as np

a = 0.5
b = 1.0
E = 0.0001

f = lambda x: x**2 - np.sin(x)

N = int(( np.log( b - a ) - np.log( E ) ) / np.log(2))

def bisection(x0,x1,e):
    step = 1
    print('\n\n====BISECTION METHOD====')
    condition = True
    print('| Iteration|      a        |      b        |      x2       |      f(x2)     |')

    while condition:
        x2 = (x0 + x1)/2
        print('| %d        |   %0.4f      |   %0.4f      |   %0.4f      |   %0.4f      |' % (step, x0, x1, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e
    
    print('\nRoot is : %0.3f' % x2)

if f(a) * f(b) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(a,b,E)