#! -*- coding: UTF-8 -*-
import tensorflow as tf
import numpy as np
import string, re

# General variables.
hiddenLayerSize = 256
learningRate = 0.01

# All valid characters.
alphabet = string.ascii_lowercase + "ğöçıüş"
alphabetSize = len(alphabet)

languages = ["English", "Turkish"]
languageCount = len(languages)

# Word filter. Deletes unwanted char from given string.
def wordFilter(x):
	# String only can contain lowercase, uppercase letters, Turkish alphabet letters and spaces.
	x = re.sub(r"""[^a-zğöçıüş]""", "", x)
	x = x.strip()
	return x

# xx_n has shape (Batch, Timestep)
# yy_n has shape (Batch)

# xx_n has integers for each timestep, which going to be converted to one-hot vector with xx tensor.
# yy_n has just an 1 integer for last timestep. (Many-to-One)
# Also this is going to be converted to one-hot vector with yy tensor.
xx_n = tf.placeholder(tf.int32, shape=(None, None))
yy_n = tf.placeholder(tf.int32, shape=(None))

xx = tf.one_hot(xx_n, alphabetSize)
yy = tf.one_hot(yy_n, languageCount)

# BasicLSTMCell used as RNN cell.
lstm_cell = tf.nn.rnn_cell.BasicLSTMCell(hiddenLayerSize)
out, state = tf.nn.dynamic_rnn(lstm_cell, xx, dtype=tf.float32)
logits = tf.layers.dense(out, units=languageCount)

# All we care about is last output of the network. (Many-to-One)
lastOutput = logits[0][-1]

# This loss function takes input, applies Softmax to it.
# And calculates loss from given target values.
loss = tf.losses.softmax_cross_entropy(logits=lastOutput, onehot_labels=yy)
optimizer = tf.train.AdamOptimizer(learningRate)
train = optimizer.minimize(loss)

# This tensor going to be used in testing.
# Softmax is already calculating by loss function during training.
prediction = tf.nn.softmax(lastOutput)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

# Load previously trained model.
saver = tf.train.Saver()
try:
	saver.restore(sess, 'model/weights')
	print("Weights loaded.")
except:
	print("Weights not found. Exiting.")
	exit()

sess.run(tf.global_variables_initializer())

# Let's test our model by hand.
while True:
	inW = wordFilter(input(">> "))

	xx = []
	for inL in inW:
		xx.append(alphabet.index(inL))
	xx = np.array(xx)

	batch_x = xx
	batch_x = batch_x.reshape((1,) + batch_x.shape)

	feed = {
		xx_n:batch_x
	}

	pred = sess.run(prediction, feed_dict=feed)
	for i, lang in enumerate(languages):
		print(lang + ": %" + ("%.2f" % (pred[i]*100)))

	langText = languages[np.argmax(pred)]

	print(inW, langText)
	print("-----------------------")