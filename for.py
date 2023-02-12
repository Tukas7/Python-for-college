from random import randint
s=0
n=int(input())
for i in range(n):
    a= randint(1,10)
    s+=a
    print(a, end=' ')
print()
print(s)