a = [56,2,13,1,78,4,6]
n=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]>a[i]:
            a[j],a[i]=a[i],a[j]
print(a)        