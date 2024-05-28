a = [2,5,1,7,8]

b = []
c = []

for i in range (0, len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
    else:
        c.append(a[i])

print(b,c)