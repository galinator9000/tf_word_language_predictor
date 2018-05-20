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

# Some examples below. (After 10.000 epochs training)
```
>> basic
English: %99.9
Turkish: %0.0848
basic English
-----------------------
>> word
English: %1e+02
Turkish: %6.12e-17
word English
-----------------------
>> level
English: %98.8
Turkish: %1.21
level English
-----------------------
>> tahmin
English: %21.9
Turkish: %78.1
tahmin Turkish
-----------------------
>> natural
English: %99.3
Turkish: %0.701
natural English
-----------------------
>> language
English: %99.8
Turkish: %0.229
language English
-----------------------
>> doğal
English: %82.7
Turkish: %17.3
doğal English
-----------------------
>> dil
English: %96.4
Turkish: %3.64
dil English
-----------------------
>> işleme
English: %5.73e-08
Turkish: %1e+02
işleme Turkish
-----------------------
```
