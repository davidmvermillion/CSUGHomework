# Initial code from Module 2 Critical Thinking Page
# https://csuglobal.instructure.com/courses/99352/assignments/1879939?module_item_id=5094314
from os import chdir
from os.path import abspath, dirname
import tensorflow.compat.v1 as tf
import matplotlib.pyplot as plt
import numpy as np

# Force script execution directory to current path
chdir(dirname(abspath(__file__)))

# Disable V2 actions
# https://www.kaggle.com/discussions/general/219215
tf.disable_v2_behavior()

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

# Load and Prep Data
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

# Show Sample Image
display_sample(1234)

# Check Data
plt.imshow(images, cmap=plt.get_cmap('gray_r'))
plt.show()

# Placeholders
input_images = tf.placeholder(tf.float32, shape=[None, 784])
target_labels = tf.placeholder(tf.float32, shape=[None, 10])

# Network Parameters
input_layer = tf.matmul(input_images, input_weights)
hidden_layer = tf.nn.relu(input_layer + input_biases)
digit_weights = tf.matmul(hidden_layer, hidden_weights) + hidden_biases
loss_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=digit_weights, labels=target_labels))
optimizer = tf.train.GradientDescentOptimizer(0.5).minimize(loss_function)
correct_prediction = tf.equal(tf.argmax(digit_weights,1), tf.argmax(target_labels,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Train Model
tf.global_variables_initializer().run()
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