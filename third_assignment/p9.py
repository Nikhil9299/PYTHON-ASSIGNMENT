a = "I need to work very hard to learn more about algorithms in Python!"
s=''
for i in a:
    if i.isalnum() or i==" ":
        s+=i
w=s.split()
avg=sum(map(len,w))/len(w)
print(round(avg,4))