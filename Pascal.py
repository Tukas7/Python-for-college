n=int(input())
a=[]
for i in range (n+1):
    a.append([1]+[0]*n)
for i in a:
    print(i)
for i in range (1,n+1):
    for j in range(1,n+1):
        a[i][j]=a[i-1][j]+a[i-1][j-1]
for i in range (0,n+1):
    for j in range (0,n+1):
        print(a[i][j], end='')
    print()