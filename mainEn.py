import json
import re
import operator

def getNewEnglishWordsList(list, word):
    data = word.lower()

    if list.get(data) != None:
        list.update({data: list[data] + 1})
    else:
        list.update({data: 1})

jsonEnData = open("en.json", "r")
jsonLines = []

for line in jsonEnData:
    jsonLines.append(line)

jsonWordsList = []

for line in jsonLines:
    jsonWordsList.append(json.loads(line))

jsonWordsParsedList = []
for jsonData in jsonWordsList:
    jsonWordsParsedList.append({'id': jsonData['id'],
                           'title': re.findall(r"[\w']+", jsonData['title']),
                           'body': re.findall(r"[\w']+", jsonData['body'])})

extractedEnWords = {}

for data in jsonWordsParsedList:
    for title in data['title']:
        getNewEnglishWordsList(extractedEnWords, title)
    for body in data['body']:
        getNewEnglishWordsList(extractedEnWords, body)

result = open("94463104_Assignment2_Part1_EN.en", "w+")

for i in range(0, 1000):
    key = max(extractedEnWords.items(), key=operator.itemgetter(1))[0]
    token = extractedEnWords.pop(key)
    result.write(str(i) + ')' + key + ': ' + str(token) + '\n')
