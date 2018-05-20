#! -*- coding: UTF-8 -*-

'''
Creates Numpy array with vocabularies.
Just stores index of onehot vector instead of storing onehot vectors.
'Index to onehot vector' conversion done by TensorFlow during training. (tf.one_hot function)
'''

import numpy as np
import string

# All valid characters.
alphabet = string.ascii_lowercase + "ğöçıüş"
alphabetSize = len(alphabet)

# Applies filter to given list. (Deletes empty elements from list.)
def applyFilter(x):
	return list(filter(None, x))

en = applyFilter(open("english.txt", "r", encoding="utf-8").read().split("\n"))
tr = applyFilter(open("turkish.txt", "r", encoding="utf-8").read().split("\n"))

enCount = len(en)
trCount = len(tr)

print("English vocabulary size:", enCount)
print("Turkish vocabulary size:", trCount)

X = []
y = []

# For all English words.
for enW in en:
	xx = []

	# Checks if current word appears in other languages or not.
	if enW in tr:
		print("[!] Duplicated word:", enW)
		continue

	# For all letters in that word.
	for enL in enW:
		# Add them as alphabet index to a list.
		xx.append(alphabet.index(enL))

	if len(xx) > 0:
		# Convert list to Numpy array.
		xx = np.array(xx)

		X.append(xx)
		y.append(0)

# For all Turkish words.
for trW in tr:
	xx = []

	# Checks if current word appears in other languages or not.
	if trW in en:
		print("[!] Duplicated word:", trW)
		continue

	# For all letters in that word.
	for trL in trW:
		xx.append(alphabet.index(trL))

	if len(xx) > 0:
		# Convert list to Numpy array.
		xx = np.array(xx)

		X.append(xx)
		y.append(1)

# Convert lists to a Numpy arrays.
X = np.array(X)
y = np.array(y)

# Shuffle the array.
rand = np.arange(X.shape[0])
np.random.shuffle(rand)
X = X[rand]
y = y[rand]

print(X.shape)
print(y.shape)

# Save them.
np.save("X", X)
np.save("y", y)