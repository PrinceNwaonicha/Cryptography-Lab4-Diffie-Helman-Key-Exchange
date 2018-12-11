'''
First I calculated the bit length of 10000000 and 1000000000 respectively(10million and 1billion).
10million
10^7 = 2^x---- 7 = xlog(2) ------ 7/log(2) = x ----- 23.2535 = x bits

1billion
10^9 = 2^x---- 9 = xlog(2) ------ 9/log(2) = x ----- 29.8974 = x bits




'''

import random
import secrets
'''
UserInput = input("")
UserInput = int(UserInput)
'''
def Fermat_Tester(n):
    if n < 3:
        return False
    for i in range(0, 20):
        a = random.randint(2, n-2)
        if pow(a,n-1,n) != 1:
            return False
        return True



def Safe_Prime(Prime):
    q,r = divmod((Prime - 1),2)
    qresullt = Fermat_Tester(q)
    if qresullt:
        return True, q
    else:
        return False, q

def Odd(n):
    num,r = divmod(n,2)
    if r == 0:
        return False
    else:
        return True

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







g2 = 1
gq = 1
while g2 == 1 and gq == 1:
    c = secrets.randbelow(61866083)
    g2 = SquareAndMultiply(c,30933041,61866083)
    gq = SquareAndMultiply(c,30933041,61866083)
    if g2 != 1 and gq != 1:
        print(c)
'''
#def generator(g,p,q):
    
getbits = secrets.randbits(29)
presult = Fermat_Tester(getbits)

while not presult:

    getbits = secrets.randbits(29)
    presult = Fermat_Tester(getbits)
    if presult:
        qresult, N = Safe_Prime(getbits)
        if qresult == False:
            presult = False
print(getbits)
print(qresult)
print(presult)
print(N)
'''
