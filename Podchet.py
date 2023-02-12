a=[0,1,2,3,4,2,3,4,3,2,1,2,3,4,2]
count=[0]*6
for i in a:
    count[i]+=1
print(count)
for i in range(6):
    if count[i]>0:
        print(str(i)*count[i])