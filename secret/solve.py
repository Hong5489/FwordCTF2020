from pwn import *
a = []
p = remote("secretarray.fword.wtf", 1337)
p.recvuntil("START:\n")
p.sendline("0 1")
x = int(p.recvuntil("\n")[:-1])
p.sendline("0 2")
y = int(p.recvuntil("\n")[:-1])
p.sendline("1 2")
z = int(p.recvuntil("\n")[:-1])
a.append((x + y - z)//2)
a.append(x - a[0])
a.append(z - a[1])

for i in range(3,1337):
	p.sendline("0 %i"%(i+1))
	a.append(int(p.recvuntil("\n")[:-1])-a)
	print(i)

ans = "DONE"
for i in range(1337):
	ans += " " + str(a[i])
p.sendline(ans)
p.interactive()