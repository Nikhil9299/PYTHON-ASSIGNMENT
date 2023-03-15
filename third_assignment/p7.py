s ="adfw$vf&yvy*ugv%uy"
a=[]
p=[]
for i in s:
    if i.isalnum():
        a.append(i)
    else:
        p.append(i) 

a.reverse()

r=[]
for i in s:
    if i.isalnum():
        r.append(a.pop(0))
    else:
        r.append(p.pop(0))
f="".join(r)
print(f)            