from random import randrange
from Crypto.Util.number import getStrongPrime

p = getStrongPrime(512)
q = getStrongPrime(512)
n = p * q
e = randrange(2**16,2**1024)

plain = open('plaintext','r').read().lower()
arr = []
for i in plain:
	arr.append(pow(ord(i),e,n))
open('encrypted','w').write(str(n)+"\n"+str(arr))
