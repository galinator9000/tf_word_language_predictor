#! -*- coding: UTF-8 -*-
import string, re

'''
Takes the raw vocabulary files and creates own. (Deletes unwanted characters...)
'''

alphabet = string.ascii_lowercase + "ğöçıüş"
alphabetSize = len(alphabet)

# Applies filter to given list. (Deletes empty elements from list.)
def applyFilter(x):
	return list(filter(None, x))

# Word filter. Deletes unwanted char from given string.
def wordFilter(x):
	# String only can contain lowercase letters and Turkish alphabet letters.
	x = re.sub(r"""[^a-zğöçıüş]""", "", x)
	x = x.strip()
	return x

# English raw vocabulary uses \r\n as newline.
# Turkish raw vocabulary uses \n as newline.
en = open("englishRaw.txt", "r", encoding="utf-8").read().replace("\r\n", "\n")
tr = open("turkishRaw.txt", "r", encoding="utf-8").read()

# Vocabularies gonna be size of approximately this value.
approxVocabSize = 25000

enList = applyFilter(en.split("\n"))
trList = applyFilter(tr.split("\n"))

enCount = len(enList)
trCount = len(trList)

enSkip = int(enCount / approxVocabSize)
trSkip = int(trCount / approxVocabSize)

if approxVocabSize > enCount or approxVocabSize > trCount:
	print("Vocabulary size should be smaller than raw vocabulary size.")
	exit()

# New files.
enW = open("../english.txt", "w", encoding="utf-8")
trW = open("../turkish.txt", "w", encoding="utf-8")

ee = 0
tt = 0

for e in range(0, enCount, enSkip):
	w = wordFilter(enList[e])

	enW.write(w + "\n")
	ee += 1

for t in range(0, trCount, trSkip):
	# Turkish raw vocabulary have 2 'thing' in each line, seperated with space.
	# We're interested in just words, not others. So split with space and get first value.
	w = wordFilter(trList[t].split(" ")[0])

	trW.write(w + "\n")
	tt += 1

print("English raw vocabulary size:", enCount)
print("Turkish raw vocabulary size:", trCount)

print("English final vocabulary size:", ee)
print("Turkish final vocabulary size:", tt)

trW.close()
enW.close()