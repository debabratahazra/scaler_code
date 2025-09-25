# objective function used for gradient descent is (x-1)²
# x-> input value

'''
v(t+1) = β*v(t) + (1-β)*(∂f/∂x)

where β = momentum constant (fix value as 0.9)
      f = objective fuction(the function over which gradient descent is being applied)
v(t) is the value of v at a certain iteration 't'.


x(t+1) = x(t) - α*v(t+1)

where α = learning rate (fix value as 0.01)
x(t) is the value of input 'x' at a certain iteration 't'.
'''


def obj_func(x):
    return (x * x - 2 * x + 1)
    
# code starts here

"""
set value of 'alpha' as 0.01 and 'beta' as 0.9
"""
alpha = 0.01
beta = 0.9

def grad(x):
    # return the gradient of the objective function
    return (2 * x - 2)
 
"""
set value of iterations to 4
"""
iterations = 4

# function of momentum based gradient descent
def momentum(x):

    # initalize value of v to zero
    v = 0
    for i in range (iterations):
    
        # write code to update the value of v on every iteration
        v = beta * v + (1 - beta) * grad(x)
        
        # write code to update the value of x on every iteration
        x = x - alpha * v

    # finally return the value of x and obj_func(x)
    return x, obj_func(x)

# code ends here