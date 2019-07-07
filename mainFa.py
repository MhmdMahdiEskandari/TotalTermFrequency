import json
import re
import operator

def getNewPersianWordsList(list, word):
    data = getAsciiOfPersianWord(word)

    if list.get(data) != None:
        list.update({data: list[data] + 1})
    else:
        list.update({data: 1})

def getAsciiOfPersianWord(word):
    data = word.replace('\u064a', '\u06cc').replace('\u0622', '\u0627').replace('\u0643', '\u06a9')
    return data

jsonFaData = open("fa.json", "r", encoding='utf-8')
jsonLines = []

for line in jsonFaData:
    jsonLines.append(line)

jsonWordsList = []

for line in jsonLines:
    jsonWordsList.append(json.loads(line))

jsonWordsParsedList = []
for data in jsonWordsList:
    jsonWordsParsedList.append({'id': data['id'],
                           'title': re.findall(r"[\u0620-\u065F\u0670-\u06ff]+", data['title']),
                           'body': re.findall(r"[\u0620-\u065F\u0670-\u06ff]+", data['body'])})

extractedFaWords = {}

for data in jsonWordsParsedList:
    for title in data['title']:
        getNewPersianWordsList(extractedFaWords, title)
    for body in data['body']:
        getNewPersianWordsList(extractedFaWords, body)

result = open("94463104_Assignment2_Part1_FA.fa", "w+", encoding='utf-8')

for i in range(0, 1000):
    key = max(extractedFaWords.items(), key=operator.itemgetter(1))[0]
    token = extractedFaWords.pop(key)
    result.write(str(i) + ')' + key + ': ' + str(token) + '\n')