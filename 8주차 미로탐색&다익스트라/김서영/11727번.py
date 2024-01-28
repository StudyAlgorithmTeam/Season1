x = input()
y = input()
z = []

for i in range(len(x+y)-1):
    z.append((int(x[(i+1)//2])+int(y[i//2]))%10)

while len(z) != 2:
    a = []
    for i in range(len(z)-1):
        a.append((z[i]+z[i+1])%10)
    z = a

print(str(z[0])+str(z[1]))
