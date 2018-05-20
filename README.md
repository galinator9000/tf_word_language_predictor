# tf_word_language_predictor
Basic character-level word language predictor (English-Turkish) with Many-to-One LSTM written in TensorFlow.

# Data
`
processRaw.py
`

Processes raw vocabulary files. Creates a new file, writes each word line by line to created files.

`
createArray.py
`

Takes processed vocabulary files and creates Numpy matrices named as "X.npy" and "y.npy" with them.

Features are just index number of the alphabet of the current letter.

During feeding to the model, these are converted to one hot vectors. (tf.one_hot function)

`
train.py
`

Loads X.npy and y.npy and trains the model.

# Some examples below.
