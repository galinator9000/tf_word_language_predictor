# tf_word_language_predictor
Basic character-level word language predictor (English, Turkish) with Many-to-One LSTM written in TensorFlow.

<h2>Data sources
<h4>Turkish: https://code.google.com/archive/p/zemberek/downloads (1140208 Turkish words)
<h4>English: https://github.com/dwyl/english-words (370099 English words)

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
After 10.000 epochs training, trained with ~50000 words. (~25000 for each language)
```
English: %98.04
Turkish: %1.96
hypophysectomize English
-----------------------
English: %99.99
Turkish: %0.01
playwrightess English
-----------------------
English: %99.62
Turkish: %0.38
footings English
-----------------------
English: %30.09
Turkish: %69.91
seminule Turkish
-----------------------
English: %0.00
Turkish: %100.00
ağırlaşmasında Turkish
-----------------------
English: %0.00
Turkish: %100.00
unutmadığımın Turkish
-----------------------
English: %15.65
Turkish: %84.35
cezbeden Turkish
-----------------------
English: %0.00
Turkish: %100.00
düşeceklerle Turkish
-----------------------
English: %100.00
Turkish: %0.00
unpropriety English
-----------------------
English: %95.69
Turkish: %4.31
lararia English
-----------------------
English: %99.17
Turkish: %0.83
lithotrite English
-----------------------
English: %0.00
Turkish: %100.00
savunmanızı Turkish
-----------------------
English: %0.00
Turkish: %100.00
statüsündeydiler Turkish
-----------------------
English: %0.00
Turkish: %100.00
kontratımla Turkish
-----------------------
English: %72.68
Turkish: %27.32
comtesse English
-----------------------
English: %99.17
Turkish: %0.83
greenhorns English
-----------------------
English: %0.01
Turkish: %99.99
solmazdı Turkish
-----------------------
English: %99.84
Turkish: %0.16
regaling English
-----------------------
English: %0.00
Turkish: %100.00
incinmişsin Turkish
-----------------------
English: %0.00
Turkish: %100.00
sağlamlandırmak Turkish
-----------------------
English: %0.00
Turkish: %100.00
ulaşılmışlık Turkish
-----------------------
English: %0.08
Turkish: %99.92
serenliyi Turkish
-----------------------
English: %0.00
Turkish: %100.00
durumdaymışım Turkish
-----------------------
English: %0.00
Turkish: %100.00
kaybedesiniz Turkish
-----------------------
English: %86.71
Turkish: %13.29
protephemeroidea English
-----------------------
English: %99.95
Turkish: %0.05
botchy English
-----------------------
English: %98.94
Turkish: %1.06
undersaturate English
-----------------------
English: %99.53
Turkish: %0.47
fierabras English
-----------------------
English: %99.99
Turkish: %0.01
onay English
-----------------------
English: %0.00
Turkish: %100.00
üçkağıtçıda Turkish
-----------------------
English: %51.02
Turkish: %48.98
ugli English
-----------------------
English: %0.01
Turkish: %99.99
güvenliklerle Turkish
-----------------------
English: %99.97
Turkish: %0.03
microswitch English
-----------------------
English: %100.00
Turkish: %0.00
compellability English
-----------------------
English: %9.38
Turkish: %90.62
arzuhalci Turkish
-----------------------
English: %99.77
Turkish: %0.23
psychiatrist English
-----------------------
English: %0.01
Turkish: %99.99
coşkumuzla Turkish
-----------------------
English: %0.00
Turkish: %100.00
bayılmamız Turkish
-----------------------
English: %98.25
Turkish: %1.75
tidier English
-----------------------
English: %98.58
Turkish: %1.42
hyperalgesic English
-----------------------
English: %0.00
Turkish: %100.00
kurabiyelerimiz Turkish
-----------------------
English: %36.06
Turkish: %63.94
simgeci Turkish
-----------------------
English: %0.00
Turkish: %100.00
çalışmalısınızdır Turkish
-----------------------
English: %99.76
Turkish: %0.24
reduccion English
-----------------------
```
