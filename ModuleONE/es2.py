def listSum(list):
    count = 0
    for item in list:
        count += item
    return count

print(listSum([2,4,3]))


def palindromoCheck(string):
    string2 = string[-1::-1]

    if string2 == string: return True
    else: return False

print(palindromoCheck(input()))