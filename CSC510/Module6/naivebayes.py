# Setup
from sklearn import naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data Import and Split
iris = pd.read_csv('iris.csv')
train, test = train_test_split(iris, test_size = 0.2, train_size = 0.8, random_state = 20191220, shuffle = True)
# https://www.geeksforgeeks.org/how-to-exclude-columns-in-pandas/
train_features = train.loc[:, train.columns != 'Species']
train_values = train['Species']
test_features = test.loc[:, test.columns != 'Species']
test_values = test['Species']
setosa = iris[iris['Species'] == 'Iris-setosa']
versicolor = iris[iris['Species'] == 'Iris-versicolor']
virginica = iris[iris['Species'] == 'Iris-virginica']

# Quasi-Frequency Tables
# https://stackoverflow.com/a/69931523/13801562
setosa.loc[:, versicolor.columns != 'Id'].describe().map(lambda x: f"{x:0.3f}")
versicolor.loc[:, versicolor.columns != 'Id'].describe().map(lambda x: f"{x:0.3f}")
virginica.loc[:, versicolor.columns != 'Id'].describe().map(lambda x: f"{x:0.3f}")

# Build Gaussian Naive-Bayes Classification Model
# https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes
classifier = naive_bayes.GaussianNB()
prediction = classifier.fit(train_features, train_values).predict(test_features)
print("Out of %d total points, %d were mislabled"
      % (test_features.shape[0], (test_values != prediction).sum()))

# Display Confusion Matrices of Test Results
# https://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
titles_options = [
    ("Confusion Matrix of Test Values", None),
    ("Test Value Probabilities", "true"),
]
for title, normalize in titles_options:
    disp = ConfusionMatrixDisplay.from_estimator(
        classifier,
        test_features,
        test_values,
        display_labels = iris['Species'].unique(),
        cmap = plt.cm.Greens,
        normalize = normalize,
    )
    disp.ax_.set_title(title, fontsize = 23, pad = 15).set_color('#171819')
    disp.ax_.set_xlabel('Predicted Label', fontsize = 15, loc =
				'left').set_color('#707070')
    disp.ax_.set_ylabel('True Label', fontsize = 15, rotation =
				'horizontal', loc = 'bottom', labelpad =
				15).set_color('#707070')
    # https://stackoverflow.com/a/52472732/13801562
    plt.box(False)
    disp.ax_.tick_params(axis='y', which='both', right=False,
				left=False, colors = '#686868')
    disp.ax_.tick_params(axis='x', which='both', top=False,
				bottom=False, colors = '#686868')