l = [1,None,None,3,None,4]
for i in range(len(l)):
    if l[i] is None:
        l[i]=(l[i-1])
print(l)        