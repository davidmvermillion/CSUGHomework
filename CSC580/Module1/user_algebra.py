from sklearn.linear_model import LinearRegression
from random import randint
from os import chdir
from os.path import abspath, dirname

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Request user input
# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
initial = list(map(int, input("Enter 4 to 8 integers separated by spaces: ").split()))

# Create training data
train_set_limit = 1000
train_set_count = 100

train_input = list()
train_output = list()
variable_names_full = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
variables = list()

for i in range(train_set_count):
    for k in len(range(initial)):
        variables[i] = randint(0, train_set_limit)

# possibly if/else statements for each case

'''
For this assignment, implement a Python program that allows the user to enter coefficients
for a linear equation that contains between four and eight variables.
Next, train a model that “fits” the linear equation.
Finally, prompt the user for a set of input numbers to test the model.
Print out the predicted value and the actual value.
'''