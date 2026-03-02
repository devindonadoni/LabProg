def quadratoECubo():
    print("Enter number")
    x = int(input())
    print(pow(x, 2), pow(x, 3))

def orarioConverter(minuti):
    ore = 0
    while minuti >= 60:
        minuti -= 60
        ore += 1
    print(f"{ore}h:{minuti}min")

def pariDispari():
    print("Enter number")
    x = int(input())
    if x%2 == 0:
        print("pari")
    else:
        print("dispari")

def checkLetter(parola, lettera):
    count = 0
    for i in parola:
        if i == lettera: count += 1 
    print(count)

def checkPrimo():
    numero = int(input())
    primo = 1

    for i in range(2, numero-1, 1):
        if numero % i == 0:
            primo = 0

    print(primo)

def sumN():
    n = 1
    result = 0
    while n != 0:
        n = int(input())
        result += n

    print(result)

def fattoriale():
    x = int(input())
    result = 1
    for i in range(1, x+1):
        result *= i
    print(result)


def checkTriangle():
    a = int(input())
    b = int(input())
    c = int(input())

    if(a + b > c and a + c > b and b + c > a ):
        if a == b == c: 
            print("equi")
        elif a != b != c:
            print("scaleno")
        else:  
            print("iso")
        
def vocali():
    parola = input()
    vocali = "aeiouAEIOU"
    count = 0

    for char in parola:
        if char in vocali:
            count += 1

    print(count)