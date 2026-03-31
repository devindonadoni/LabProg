def countOccorrenze(file, list):
    wordDict = {}
    for word in file.read().split():
        if word in list:
            if word in wordDict.keys():
                x = wordDict.get(word)
                wordDict.update({word: x + 1})
            else:
                wordDict.update({word : 1})
    
    return wordDict

def listSum(list):
    sum = 0
    for number in list:
        sum += number
    return sum

def palindromo(string):
    gnirts = string[::-1]
    print(gnirts)
    if(gnirts == string):
        return True
    else:
        return False

def scambia(i, j , list):
    tmp = list[i]
    list[i] = list[j]
    list[j] = tmp
    return list

def checkLists(list1, list2):
    for item in list1:
        for item2 in list2:
            if item == item2:
                return True
    return False

def numberToString(list):
    myDict = {1: 'uno', 2: 'due', 3: 'tre', 4: 'quattro', 5: 'cinque', 6: 'sei', 7: 'sette', 8: 'otto', 9: 'nove', 0: 'zero'}
    newList = []
    for item in list:
        newList.append(myDict.get(item))
    return newList

#! es1-2
# wordList = ["ciao", "sofi", "ai", "fra"]
# with open("es3Re.txt", 'r') as file:
#     print(countOccorrenze(file, wordList))

#! es1-1
# listN = [1,2,4,8]
# print(listSum(listN))

#! es2-1
# stringa = "aiax"
# print(palindromo(stringa))

#! es3-1
# list = [0, 1, 2, 3]
# print(scambia(0, 3, list))

#! es4-1
# list = [0, 1, 2, 3]
# list2 = [90, 12, 44, 5]
# print(checkLists(list, list2))

#! es5-1 
# nList = [5,8,9,3,2,5,6,7,8,1]
# print(numberToString(nList))


#con .read() legge carattere per carattere, compresi spazi e punteggiatura
#       usare .split("") per avere parole uniche splittate in base agli spazi