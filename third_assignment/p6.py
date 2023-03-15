f=open("p6.txt",'r')
a=f.read().splitlines()

s=''
s2=''
a1=a[0]
a2=a[1]
for i in a1:
    if i.isdigit():
            s+=i
for i in a2:
    if i.isdigit():
        s2+=i
r=int(s)+int(s2)
print(r)
