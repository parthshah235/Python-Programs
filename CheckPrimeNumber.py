import math
N=int(raw_input())
i=N
def simplePrimaryTest(number):
    if number == 2:
       return true
    if number % 2 == 0:
        return False
    i = 3
    sqrtOfNumber = math.sqrt(number) 
    while i <= sqrtOfNumber:
        if number % i == 0:
            return False
        i = i+2
    return True  
while i>=N:
    if simplePrimaryTest(i)==True:
        print i-N
        break
