# Initial code from Module 2 Critical Thinking Page
# https://csuglobal.instructure.com/courses/99352/assignments/1879939?module_item_id=5094314
from random import randint
from sklearn.linear_model import LinearRegression
from pickle import dump
from os import chdir
from os.path import abspath, dirname
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Variables
hidden_nodes = 512
input_weights = tf.Variable(tf.truncated_normal([784, hidden_nodes]))
input_biases = tf.Variable(tf.zeros([hidden_nodes]))
hidden_weights = tf.Variable(tf.truncated_normal([hidden_nodes, 10]))
hidden_biases = tf.Variable(tf.zeros([10]))

# Functions
def display_sample(num):

    #Print the one-hot array of this sample's label
    print(y_train[num]) 

    #Print the label converted back to a number
    label = y_train[num].argmax(axis=0)

    #Reshape the 768 values to a 28x28 image
    image = x_train[num].reshape([28,28])

    plt.title('Sample: %d  Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()

# display_sample(1234)


# Load data
sess = tf.InteractiveSession()
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

train_images = x_train.reshape(60000, 784)
test_images = x_test.reshape(10000, 784)
train_images = train_images.astype('float32')
test_images = test_images.astype('float32')

x_train, x_test = train_images / 255.0, test_images / 255.0

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

images = x_train[0].reshape([1,784])

for i in range(1, 500):
    images = np.concatenate((images, x_train[i].reshape([1,784])))

plt.imshow(images, cmap=plt.get_cmap('gray_r'))
plt.show()

input_images = tf.placeholder(tf.float32, shape=[None, 784])
target_labels = tf.placeholder(tf.float32, shape=[None, 10])


input_layer = tf.matmul(input_images, input_weights)
hidden_layer = tf.nn.relu(input_layer + input_biases)
digit_weights = tf.matmul(hidden_layer, hidden_weights) + hidden_biases
loss_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=digit_weights, labels=target_labels))
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss_function)
correct_prediction = tf.equal(tf.argmax(digit_weights,1), tf.argmax(target_labels,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))


EPOCH = 20
BATCH_SIZE = 100
TRAIN_DATASIZE,_ = x_train.shape
PERIOD = TRAIN_DATASIZE//BATCH_SIZE

 

for e in range(EPOCH):
    idxs = np.random.permutation(TRAIN_DATASIZE)
    X_random = x_train[idxs]
    Y_random = y_train[idxs]

    for i in range(PERIOD):
        batch_X = X_random[i * BATCH_SIZE:(i+1) * BATCH_SIZE]
        batch_Y = Y_random[i * BATCH_SIZE:(i+1) * BATCH_SIZE]
        optimizer.run(feed_dict = {input_images: batch_X, target_labels:batch_Y})

    print("Training epoch " + str(e+1))
    print("Accuracy: " + str(accuracy.eval(feed_dict={input_images: x_test, target_labels: y_test})))

# Instructions
'''
For this assignment, you will use TensorFlow with Python. This assignment assumes you have read
relevant literature and have TensorFlow installed.

The standard example for machine learning these days is the MNIST data set, a collection of
70,000 handwriting samples of the numbers 0-9. Your task is to predict which number each
handwritten image represents.

Each image is 28x28 grayscale pixels, so you can treat each image as just a 1D array, or tensor,
of 784 numbers. As long as you're consistent in how you flatten each image into an array,
it will still work.

Start by importing the data set, which conveniently is part of TensorFlow itself:

----

MNIST provides 60,000 samples in a training data set, 10,000 samples in a test data set,
and 5,000 samples in a "validation" data set. Validation sets are used for model selection,
so you use validation data to select your model, train the model with the training set,
and then evaluate the model using the test data set.

The training data, after you "flatten" it to one dimension using the reshape function,
is therefore a tensor of shape [60,000, 784]: 60,000 instances of 784 numbers that
represent each image.

Next, encode the label data as "one_hot" by calling the to_categorical function.

Define a function to visualize what the input data looks like,
and pick a random training image to see what it is you\’re up against:

----

While training, you'll assign input_images to the training images and target_labels
to the training labels. While testing, you'll use the test images and test labels instead.

----
Now, you’ll set up your deep neural network. You'll need an input layer with one node
per input pixel per image, or 784 nodes. That will feed into a hidden layer of some
arbitrary size, so pick 512. That hidden layer will output 10 values, corresponding
to scores for each classification to be fed into softmax.

You'll need to reserve variables to keep track of all the weights and biases for both layers:

----

Next, feed that into the hidden layer, which applies the ReLU activation function to the
weighted inputs with the learned biases added in as well.

 

Finally, the output layer, called digit_weights, multiplies in the learned weights of the
hidden layer and adds in the hidden layer's bias term.

----

Next, define the loss function for use in measuring progress in gradient descent: cross-entropy,
which applies a logarithmic scale to penalize incorrect classifications much more than ones
that are close.

----

Now, set up the gradient descent optimizer, initializing it with an aggressive learning rate (0.5)
and the loss function defined above. That learning rate is an example of a hyperparameter that
may be worth experimenting with and tuning.

----

Next, train the neural network and measure its accuracy. First, define some methods for
measuring the accuracy of our trained model.

correct_prediction will look at the output of the neural network (in digit_weights),
choose the label with the highest value, and see if that agrees with the target label given.

accuracy then takes the average of all the classifications to produce an overall score
for our model's accuracy.

Now, it’s time to train the model. Set up a TensorFlow session and initialize the variables.
Next, train the network in 20 steps (or "epochs") with batches of 100 samples from the training data.

----

After you train your model, answer the following questions.
You may have to write a Python script to answer a particular question.

What is the accuracy of the model?
What are some of the misclassified images?
How is the accuracy affected by using more hidden neurons? Fewer hidden neurons?
How is the accuracy affected by using different learning rates? Try a range of at least four values.
How is accuracy affected by adding another hidden layer?
How is accuracy affected by using different batch sizes? Try at least three different batch sizes.
What is the best accuracy you can get from this multi-layer perceptron?
Summarize your findings in a Word document.
For each finding, include the Python code and screenshots of the run-time output.
Submit your Word document and Python source files as a zip file with the name:

CSC526_CTA_2_1_last_name_first_name.zip.

Your paper should be a minimum of two pages in length and conform to the CSU Global Writing Center.
The Writing Center can be easily accessed by clicking on the tab in the course navigation panel.

'''