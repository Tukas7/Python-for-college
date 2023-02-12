a=[123,213,22,3,4,5,6]
while len(a)>0:
  last=a.pop()
  if last%2==0:
      print('Yes', last)
      break
else:
    Print('No')