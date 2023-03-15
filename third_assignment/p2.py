a=[1,2,3,4,1,4,5]
s=[]
for i in a:
    if i not in s:
        s.append(i)
print(s)        