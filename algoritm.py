a=int(input())
b=int(input())
while b>0:
    c=a%b
    a=b
    b=c
print(a)