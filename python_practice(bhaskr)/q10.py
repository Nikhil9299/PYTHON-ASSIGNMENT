a="MsYs TecHNOlogiEs iS a gREat place To woRk"
small=0
cap=0
for i in range(len(a)):
    if a[i].islower():
        small+=1
    elif a[i].isupper():
        cap+=1    
print(cap)        
print(small)