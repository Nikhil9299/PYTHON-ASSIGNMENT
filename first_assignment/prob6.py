a="nikhilkp"
length=len(a)//2
s1=a[:length]
s2=a[length:]
s=s1[::-1]
ss=s2[::-1]
st=s+ss
print(st)
#(or)
a="nikhilkp"
s=""
p=""
q=len(a)//2
for i in range(len(a)):
    if i<=(q-1):
        s=s+a[i]
    else:
        p=p+a[i]
d=s+p        
print(s)
print(p)