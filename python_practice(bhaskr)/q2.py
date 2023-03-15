n=[1,2,3,4,5,6,7,8,9,10]
a=[]
for i in n:
    if i%2==0:
        a.append(i**2)
    else:
        a.append(i**3)
print(a)            