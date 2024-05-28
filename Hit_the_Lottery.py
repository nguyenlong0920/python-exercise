n = int(input())

a = n // 100
n %= 100
b = n // 20
n %= 20
c = n // 10
n %= 10
d = n // 5
n %= 5
e = n // 1
n %= 1

print (a+b+c+d+e)