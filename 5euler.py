import math

prime = [2, 3, 5, 7, 11, 13, 17, 19]

def FindRest(x):
    for i in prime:
        if x % i == 0:
            rest = x/i
            break
    return [rest, i]
            

def ArrayMultiples(x):
    num = x
    arr = []
    while True:
        if num == 1 :
            break
        out = FindRest(num)
        num = out[0]
        arr.append(out[1])
    return arr


def RemoveRedundence(arr):
    arrToDo = []
    finalArr = []
    for i in prime:
        for j in arr:
            for k in j:
                if k == i:
                    arrToDo.append(j)
                    break
        finalArr.append(ArrFight(arrToDo, i))
    return finalArr


def ArrFight(arr, joustNum):
    highestCount = 0
    for i in arr :
        count = 0
        for j in i :
            if j == joustNum:
                count += 1
        if highestCount < count :
            highestCount = count
    return(math.pow(joustNum, highestCount))

def main() :
    arr = []
    for i in range(2, 21):
        arr.append(ArrayMultiples(i)) 
    arr = RemoveRedundence(arr)
    print(arr)

    num = 1
    for j in arr:
        num *= j
    print("RESULT : " + str(num))

main()

