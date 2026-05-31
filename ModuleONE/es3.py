def es1(list):
    sum = 0
    for item in list:
        sum += item
    return sum

def es2(string):
    gnirts = string[::-1]
    return True if string == gnirts else False

def es3(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp

def es4(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

def es5(list):
    dict = {0: "zero", 1: "uno", 2: "due", 3: "tre", 4: "quattro", 5: "cinque", 6: "sei", 7: "sette", 8: "otto", 9: "nove"}
    stringList = []
    for item in list:
        stringList.append(dict.get(item))
    return stringList

def es6(list):
    newDict = {}
    for item in list:
        if item in newDict.keys():
            newDict[item] += 1
        else:
            newDict[item] = 1
    return newDict

def es7(file):
    sum = 0
    for item in file.read().splitlines():
        elements = item.split(",")
        sum = sum +  int(elements[4])
    return sum

def es8(file, parola):
    wordCount = 0
    for item in file.read().split():
        if item == parola:
            wordCount += 1
    return wordCount

def es9(file):
    newDict = {}
    for item in file.read().split():
        if item in newDict.keys():
            newDict[item] = newDict.get(item) + 1
        else:
            newDict[item] = 1
    return newDict

def es10(file):
    with open("files/unique.txt", 'w+') as fileUnique:  #w+ cancella e riscrive - a+ aggiunge alla fine
        lines = []
        for line in file.read().splitlines():
            if line not in lines:
                lines.append(line)
        
        for line in lines: 
            fileUnique.write(line + "\n") 
    

#! es1
# list = [2,3,2]
# print(es1(list))

#! es2
# string = "aiia"
# print(es2(string))

#! es3
# list = [1,2,3,4]
# print(list)
# es3(list, 0, 3)
# print(list)

#! es4
# list1 = [1,2,3,4]
# list2 = [0,8,5,6]
# print(es4(list1, list2))

#! es5
# list = [1,0,7,9,8]
# print(es5(list))

#! es6
# list = ["ciao","come","va","ciao","va", "ciao"]
# print(es6(list))

#! es7
# with open("files/shampoo.csv", 'r') as file:
#     print(es7(file))

#! es8
# with open("files/text.txt", 'r') as file:
#     print(es8(file, "aia"))

#! es9
# with open("files/text.txt", 'r') as file:
#      print(es9(file))

#! es10
with open("files/righeduplicate.txt", 'r') as file:
    es10(file)