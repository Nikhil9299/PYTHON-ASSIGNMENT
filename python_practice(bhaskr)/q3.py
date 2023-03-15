a=( "Msys", "Technologies", "2007" )
w="python"
lst=list(a)
s=[]
for i in range(len(a)):
    if i==len(a)-1:
        s.append(w)
lst.extend(s)
print(tuple(lst))


