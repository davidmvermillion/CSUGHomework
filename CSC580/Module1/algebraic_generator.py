# Initial code from Module 1 Critical Thinking Page
from random import randint
from sklearn.linear_model import LinearRegression
from skl2onnx import to_onnx
from numpy import int_
from pickle import dump
from os import chdir
from os.path import abspath, dirname

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Create training data
train_set_limit = 1000
train_set_count = 100

train_input = list()
train_output = list()

for i in range(train_set_count):
    a = randint(0, train_set_limit)
    b = randint(0, train_set_limit)
    c = randint(0, train_set_limit)
    output = a + (2*b) + (3*c)
    train_input.append([a, b, c])
    train_output.append(output)

# Create a model
predictor = LinearRegression(n_jobs = -1)
predictor.fit(X = train_input, y = train_output)

# Test model
X_test = [[10, 20, 30]]
outcome = predictor.predict(X = X_test)
coefficients = predictor.coef_
print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))

# Exporting and importing models using ONNX
# https://scikit-learn.org/stable/model_persistence.html#onnx
# https://onnx.ai/sklearn-onnx/api_summary.html
# onx = to_onnx(predictor, train_input, initial_types = int_, target_opset = 12)
# with open("filename.onnx", "wb") as f:
#     f.write(onx.SerializeToString())

# Exporting and importing models using pickle
# Note security issues suggest this should not be used for deployed models
# https://scikit-learn.org/stable/model_persistence.html#pickle-joblib-and-cloudpickle
with open("algebra.pkl", "wb") as f:
    dump(predictor, f, protocol = 5)