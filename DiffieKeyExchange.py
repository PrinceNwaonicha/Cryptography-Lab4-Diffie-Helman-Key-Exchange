'''
First I calculated the bit length of 10000000 and 1000000000 respectively(10million and 1billion).
10million
10^7 = 2^x---- 7 = xlog(2) ------ 7/log(2) = x ----- 23.2535 = x bits

1billion
10^9 = 2^x---- 9 = xlog(2) ------ 9/log(2) = x ----- 29.8974 = x bits




'''

import random
import secrets

UserInput = input("")
UserInput = int(UserInput)

#Use Fermat tester
def Fermat_Tester(n):
    if n < 3:
        return False
    for i in range(0, 20):
        a = random.randint(2, n-2)
        if pow(a,n-1,n) != 1:
            return False
        return True
#Function for finding a safe prime had to use divmod because when its not a safe prime we get floating points
def Safe_Prime(Prime):
    q,r = divmod((Prime - 1),2)
    qresullt = Fermat_Tester(q)
    if qresullt:
        return True, q
    else:
        return False, q

#Square and multiply algorithm I realized is pretty much the same as what python uses for their built in pow(b,e,m) function
def SquareAndMultiply(base,exponent,modulus):
    tempe = exponent
    tempb = base
    result = 1
    while tempe > 0:
        if tempe % 2 == 0:
            tempb = (tempb*tempb) % modulus
            tempe = tempe/2
        else:
            result = (result*tempb) % modulus
            tempe = tempe - 1
    return result

#To find the generator we check to see that
def GeneratorFinder(p,q):
    g2 = 1
    gq = 1
    while g2 == 1 and gq == 1:
        g = secrets.randbelow(p)
        g2 = SquareAndMultiply(g, 2, p)
        gq = SquareAndMultiply(g, q, p)
        if g2 != 1 and gq != 1:
            return g
        g2 = 1
        gq = 1

def GeneratePandQandG(int):
    PP = secrets.randbits(int)
    presult = Fermat_Tester(PP)
    N = 0
    while not presult:

        PP = secrets.randbits(int)
        presult = Fermat_Tester(PP)
        if presult:
            qresult, N = Safe_Prime(PP)
            if qresult == False:
                presult = False
    g = GeneratorFinder(PP,N)
    return g, PP, N

generator,Prime,Safeprime = GeneratePandQandG(UserInput)

print("We found a random integer of "+str(UserInput)+" bits.")
print("We found a random Safe Prime P which is "+str(Prime)+".")
print("We found a the smaller prime to be "+str(Safeprime)+".")
print("We found a the Generator is "+str(generator)+".")