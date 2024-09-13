from sklearn.linear_model import LinearRegression
from pickle import load
from os import chdir
from os.path import abspath, dirname

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

with open("algebra.pkl", "rb") as f:
    predictor = load(f)

X_test = [[10, 20, 30]]
outcome = predictor.predict(X = X_test)
coefficients = predictor.coef_
print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))