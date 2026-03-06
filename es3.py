def countWords(parola, file):
    count = 0
    fileReaded = file.read()
    for word in fileReaded.split():
        if parola == word:
            count += 1
    return count

def countEveryWords(file):
    words = {}
    for word in file.read().split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

def es3(file):
    words = dict()
    for word in file.read().split():
        iniziale = word[0]
        
        if iniziale not in words or len(word) > len(words[iniziale]):
            words[iniziale] = word
            
    return words

def es4(file):
    for word in file.read().replace("?", ".").replace("!", ".").strip().split("."):
        print(F"NUOVA FRASE: {word}")

f = open("file.txt", "r")
#print(countWords("ciao", f))
print(es4(f))
f.close()