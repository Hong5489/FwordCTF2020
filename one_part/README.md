# One Part ! (Crypto)
```
One part is secure ?

nc onepart.fword.wtf 4445

Author: Semah BA
```
When netcat it, it output this and disconnect:
```
nc onepart.fword.wtf 4445

	Welcome to my secure Land !!! 
	Everything is in front of you !
	test it for me before publishing it 
		
you public pair : (14033835619327792160426407352776995685845231789110003170614050617173358193723291839323197616175538343002513484796570265843480825322486634330241473579269003882368879601103217982618845822102996255412150776380761792231821930511642796978085278963536842867698347307899574769580516244937821154610288251043530916872090961808756834656792040030522636952711613489300201231655811862342155537772414683919953510903653693737773755303834628341536035891200817370415885046963126277863118921178001259745122968212220493786289219698554962272743412025360561566999866661228833595095358927534861791346621962443490677551927341827074671240141, 65537)
Bonus information 
dp : 10332164515966224149608085523390934930751379723365797446566057025103798861903008419383876935436335690978873682081580090950148591369985575306132457910009454712333071629382101229404311855959017939303582747190863284120994392360574352976183829405304037392541979029642322496944034486557379597794440606615292318049
Cipher : 11720342629419010528935099808314161261526385202646362658577238166653056152763771178189576962060613825364959438313081873535885447564581953224563070858496929722706621533977220244409478263606545461031065406345871643855433894172825091339824686616008585320387105994214774571858923268079085862756037546286161931482108954087018543704092508168588274510060311886075841878397406149719635846716181276341709990104487324687956082785179185936047042623577924971941771466773714286085547432394560754644634903453392464530687709638729749705286705599176040270858525220041719677329810622770523665782433227089964698671864881096733488068324
```
Notice each time we netcat will get a different value

It's clearly a typical **RSA challenge!**

Given public key ,ciphertext, and a `dp` value

According to [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)), dp is `d mod (p-1)`

`d` is the private key which use to decrypt the ciphertext

After some research on Google, found a [page](https://crypto.stackexchange.com/questions/46486/rsa-given-n-e-dp-is-it-possible-to-find-d) that stated we can recover the private key:

![formula](https://render.githubusercontent.com/render/math?math="gcd(n,r^{e.dp} - r mod n)")

We can calculate this in python easily:
```python
import gmpy2
p = gmpy2.gcd(n,pow(2,(e*dp),n)-2)
```
After we found `p`, we can simpily divide it with `n` and get `q`

Then we can calculate the private key `d`:
```py
p = gmpy2.gcd(n,pow(2,(e*dp),n)-2)
q = n // p
assert(n == p*q)
phi = (p-1)*(q-1)
# e^-1 mod phi
d = inverse(e,phi)
# c^d mod n
print long_to_bytes(pow(c,d,n))
```
[Full python script](solve.py)

Thats the flag!!
```
FwordCTF{i_knew_it_its_not_secure_as_i_thought}
```