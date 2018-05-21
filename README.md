# tf_word_language_predictor
Basic character-level word language predictor (English, Turkish) with Many-to-One LSTM written in TensorFlow.

<h2>Data sources
<h4>Turkish: https://code.google.com/archive/p/zemberek/downloads (1.140.208 Turkish words)
<h4>English: https://github.com/dwyl/english-words (370.099 English words)
<h4>French: https://www.kaggle.com/stephrouen/word-in-french/data (142.694 French words)

# Prepare Data

`
data/processRaw.py
`

Processes raw vocabulary files. Creates a new file, writes each word line by line to created files.

`
createArray.py
`

Takes processed vocabulary files and creates Numpy matrices named as "X.npy" and "y.npy" with them.

Features are just index number of the alphabet of the current letter.

During feed to the model, these are converted to one hot vectors. (tf.one_hot function)

`
train.py
`

Loads X.npy and y.npy and trains the model.

`
test.py
`

Loads trained model and lets the user test the model.

# Some test examples below.
After 20.000 epochs training, trained with ~75000 words. (~25000 for each language)
```
English: %10.43
Turkish: %0.33
French: %89.24
palilalie French
-----------------------
English: %99.45
Turkish: %0.13
French: %0.42
misfiled English
-----------------------
English: %0.00
Turkish: %100.00
French: %0.00
devşirmekte Turkish
-----------------------
English: %23.75
Turkish: %0.04
French: %76.21
commitments French
-----------------------
English: %0.00
Turkish: %100.00
French: %0.00
dörttede Turkish
-----------------------
English: %98.86
Turkish: %0.01
French: %1.13
injuriousness English
-----------------------
English: %16.29
Turkish: %0.28
French: %83.43
insignes French
-----------------------
English: %14.26
Turkish: %0.34
French: %85.40
tiare French
-----------------------
English: %0.00
Turkish: %0.00
French: %100.00
soulagèrent French
-----------------------
English: %0.00
Turkish: %100.00
French: %0.00
amalıyız Turkish
-----------------------
English: %0.00
Turkish: %100.00
French: %0.00
toprakları Turkish
-----------------------
English: %99.77
Turkish: %0.00
French: %0.23
dyeweeds English
-----------------------
English: %38.40
Turkish: %0.38
French: %61.21
spiderier French
-----------------------
English: %58.38
Turkish: %2.61
French: %39.00
epilachna English
-----------------------
English: %1.10
Turkish: %0.01
French: %98.89
pleuvrait French
-----------------------
English: %4.27
Turkish: %95.54
French: %0.19
yolmadan Turkish
-----------------------
English: %0.00
Turkish: %0.00
French: %100.00
cène French
-----------------------
English: %49.69
Turkish: %2.02
French: %48.28
skyscraper English
-----------------------
English: %0.01
Turkish: %0.00
French: %99.99
giboyeux French
```
