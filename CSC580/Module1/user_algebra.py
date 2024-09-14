from sklearn.linear_model import LinearRegression
from random import randint
from os import chdir
from os.path import abspath, dirname
import numberfunctions as nf
from numpy import sum, multiply

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Request user input
# https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/
# https://www.geeksforgeeks.org/how-to-get-first-n-items-from-a-list-in-python/
initial = list(map(int, input("Enter 4 to 8 integers separated by spaces: ").split()))
# Force the maximum length to 8
coefficients = initial[slice(8)]

# Create training data
train_set_limit = 1000
train_set_count = 100

if len(coefficients) == 8:
    train_in, train_out = nf.eightNumbers(train_set_count, train_set_limit, coefficients)
elif len(coefficients) == 7:
    train_in, train_out = nf.sevenNumbers(train_set_count, train_set_limit, coefficients)
elif len(coefficients) == 6:
    train_in, train_out = nf.sixNumbers(train_set_count, train_set_limit, coefficients)
elif len(coefficients) == 5:
    train_in, train_out = nf.fiveNumbers(train_set_count, train_set_limit, coefficients)
elif len(coefficients) == 4:
    train_in, train_out = nf.fourNumbers(train_set_count, train_set_limit, coefficients)
else:
    print('\nInvalid entry. Please re-run the program.\n')

# Train model
predictor = LinearRegression(n_jobs = -1)
predictor.fit(X = train_in, y = train_out)

# Test model
second = list(map(int, input("Your model was trained with {} coefficients.\nEnter {} integers separated by spaces: ".format(len(coefficients), len(coefficients))).split()))
X_test = [second]
outcome = predictor.predict(X = X_test)
# coefficients = predictor.coef_
# https://www.geeksforgeeks.org/python-multiply-two-list/
actual = sum(multiply(coefficients, second))
print('Model Outcome : {}\nActual Value : {}'.format(outcome, actual))

'''
For this assignment, implement a Python program that allows the user to enter coefficients
for a linear equation that contains between four and eight variables.
Next, train a model that “fits” the linear equation.
Finally, prompt the user for a set of input numbers to test the model.
Print out the predicted value and the actual value.
'''