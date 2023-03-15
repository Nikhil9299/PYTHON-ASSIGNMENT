
a=[5,10,15,20,25,30]
s=3
for i in range(len(a)):
    if i==s:
        a.remove(a[i])
print(a)    

#or

a=[5,10,15,20,25,30]
s=3
del a[s]
print(a)