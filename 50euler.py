import math



def primeSumMaker():
    sum = 0
    count = 0
    for num in range(2,10000000):
        prime = True
        for i in range(2, int(math.sqrt(num))):
            if (num%i==0):
                prime = False
        if prime:
            sum += num
            count += 1
        if sum > 1000000 :
            sum -= num
            count -= 1
            break
    print(sum, count)

            

primeSumMaker()
