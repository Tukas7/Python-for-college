a=input("вся строка содержащая имена, тех кто поставил лайк и тех кто оставил комментарий с разделителем в виде '/' : ")
b,c= a.split("/")
d=[]
b= b.split()
c= c.split()
for i in b:
    for g in c:
        if i == g:
            d.append(i)
print("Имена людей которые поставили лайк и оставили комментарий: ", " ".join(d))
