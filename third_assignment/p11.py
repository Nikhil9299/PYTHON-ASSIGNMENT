a = [8,9,10,"f",5,8,"d"]
c=list(map(str,a))
s=[]
for i in c:
    if i.isdigit():
        s.append(int(i)**2)
    elif i.isalpha():
        s.append(i*2)
print(s)        