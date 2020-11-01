import numpy as np

x0 = 1.0
e = 0.0001
N = 5

def f( x ): 
	return np.exp(x) - (4 * x)

def g( x ): 
	return np.exp(x) - 4

def Raphson(x0,E,N):
    print('\n\n=======NEWTON RAPHSON METHOD=======')
    step = 1
    flag = 1
    condition = True

    print('| Iteration |    x1         |     f(x1)    |')

    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)

        print('| %d         |   %0.6f    |    %0.6f  |'  % (step, x1, f(x1)))

        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')

Raphson(x0,e,N)