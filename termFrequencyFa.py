import json
import re

def splitStringToSentences(st):
    sentences = re.split(r'[.\u061f?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]


jsonData = open("fa.json", "r")
item = []

for line in jsonData:
    item.append(line)

jsonList = []

for x in item:
    jsonList.append(json.loads(x))

listOfSentences = []

for body in jsonList:
    listOfSentences.append(splitStringToSentences(body['body']))

normalizedSentences = []

for item in listOfSentences:
    for sentence in item:
        normalizedSentences.append(sentence.replace('\n', ' '))

countOfSentences = len(normalizedSentences)

sentenceLength = 0
tenLengthSentence = []

for sentence in normalizedSentences:
    length = len(sentence)
    if length == 10:
        tenLengthSentence.append(sentence)
    sentenceLength += length

averageSentenceLength = sentenceLength / countOfSentences

result = open("94463104_Assignment2_Part2_FA.fa", "w+")

result.write(str(countOfSentences) + '    ' + str(int(averageSentenceLength)) + '\n')
for i in range(0, 10):
    result.write(str(i) + ') ' + tenLengthSentence[i] + '\n')
