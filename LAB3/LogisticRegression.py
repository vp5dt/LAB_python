import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn import datasets

"""
This Digits Dataset have 569 rows [len(dataset.target)]
& 30 Columns
http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html#sklearn.datasets.load_breast_cancer
"""
# Loading Breast Cancer dataset from sklearn
dataset = datasets.load_breast_cancer()
print("(Rows, Columns)", dataset.data.shape)

# Data
data = dataset.data
# Target
target = dataset.target

# Reshaping the target array to fit the Model
target = np.array(target).reshape(569, 1)

# Setting the Placeholders to feed at the RunTime
# These should be of the Size of Dimensionality present
X = tf.placeholder(tf.float64, shape=[None, 30])
Y = tf.placeholder(tf.float64, shape=[None, 1])

# Create weight and bias, initialized to 0
w = tf.cast(tf.Variable(tf.zeros([30, 1])), tf.float64)
b = 0

# Build model to Predict Y
Y_predicted = tf.add(tf.matmul(X, w),  b)

# Passing the above to a sigmoid function to build Logistic Regression Model
Y_predicted = tf.nn.sigmoid(Y_predicted)

"""
--> Declare loss function
--> Use the sigmoid cross-entropy loss function,
--> First doing a sigmoid on the model result and then using the cross-entropy loss function
"""
loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=Y_predicted, labels=Y))

# Using gradient descent with learning rate of 0.0001 to minimize loss
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

with tf.Session() as sess:
    # Initializing Global Variables.
    sess.run(tf.global_variables_initializer())
    # For Tensor Board Graph
    writer = tf.summary.FileWriter("./graphs/logistic_reg", sess.graph)
    # Train the Model to 1600 Epochs
    for i in range(1600):
        _, acc = sess.run([optimizer, loss], feed_dict={X: data, Y: target})
        if i % 160 == 0:
            print("cost: " + str(acc))
    # Closing the File Writer
    writer.close()
    # Output the values of w
    params = sess.run(w)

# Converting to Tensor First
params = tf.convert_to_tensor(params)
data1 = tf.placeholder(tf.float64, [None, 30])
# Calculating Sigmoid function
z = tf.nn.sigmoid(tf.matmul(data1, params))
sess = tf.Session()
# Feeding the Data
prediction = sess.run(z, feed_dict={data1: data})
sess.close()

# Calculating accuracy score for the regression model
print("Accuracy Score is: {} %".format(100 - np.mean(np.abs(prediction - target)) * 100))
