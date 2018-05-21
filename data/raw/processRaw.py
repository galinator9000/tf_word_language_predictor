#! -*- coding: UTF-8 -*-
import string, re

'''
Takes the raw vocabulary files and creates own. (Deletes unwanted characters...)
'''

# Applies filter to given list. (Deletes empty elements from list.)
def applyFilter(x):
	return list(filter(None, x))

# Word filter. Deletes unwanted char from given string.
def wordFilter(x):
	x = re.sub(r"""[^a-zğöçıüşàâãèéêëîïñôöùû]""", "", x)
	x = x.strip()
	return x

# Read raw vocabularies.
en = open("englishRaw.txt", "r", encoding="utf-8").read().replace("\r\n", "\n")
tr = open("turkishRaw.txt", "r", encoding="utf-8").read().replace("\r\n", "\n")
fr = open("frenchRaw.txt", "r", encoding="utf-8").read().replace("\r\n", "\n")

# Vocabularies gonna be size of approximately this value.
approxVocabSize = 25000

enList = applyFilter(en.split("\n"))
trList = applyFilter(tr.split("\n"))
frList = applyFilter(fr.split("\n"))

# Removes duplicated words if exists.
enList = list(set(enList))
trList = list(set(trList))
frList = list(set(frList))

# Sort lists.
enList = sorted(enList)
trList = sorted(trList)
frList = sorted(frList)

enCount = len(enList)
trCount = len(trList)
frCount = len(frList)

enSkip = int(enCount / approxVocabSize)
trSkip = int(trCount / approxVocabSize)
frSkip = int(frCount / approxVocabSize)

if approxVocabSize > enCount or approxVocabSize > trCount or approxVocabSize > frCount:
	print("Vocabulary size should be smaller than raw vocabulary size.")
	exit()

# New files.
enW = open("../english.txt", "w", encoding="utf-8")
trW = open("../turkish.txt", "w", encoding="utf-8")
frW = open("../french.txt", "w", encoding="utf-8")

ee = 0
tt = 0
ff = 0

# This list will be used for storing used letters.
alphabet = []

# Process English.
for e in range(0, enCount, enSkip):
	w = wordFilter(enList[e])

	for l in w:
		alphabet.append(l)

	enW.write(w + "\n")
	ee += 1

# Process Turkish.
for t in range(0, trCount, trSkip):
	# Turkish raw vocabulary have 2 'thing' in each line, seperated with space.
	# We're interested in just words, not others. So split with space and get first value.
	w = wordFilter(trList[t].split(" ")[0])

	for l in w:
		alphabet.append(l)

	trW.write(w + "\n")
	tt += 1

# Process French.
for f in range(0, frCount, frSkip):
	w = wordFilter(frList[f])

	for l in w:
		alphabet.append(l)

	frW.write(w + "\n")
	ff += 1

alphabet = sorted(list(set(alphabet)))

alphabetF = open("../alphabet.txt", "w", encoding="utf-8")
for a in alphabet:
	alphabetF.write(a)
alphabetF.close()

print("English raw vocabulary size:", enCount)
print("Turkish raw vocabulary size:", trCount)
print("French raw vocabulary size:", frCount)

print("English final vocabulary size:", ee)
print("Turkish final vocabulary size:", tt)
print("French final vocabulary size:", ff)

trW.close()
enW.close()
frW.close()