lst = ['data','science','artificial', 'intelligence'] 
l=sorted(lst)
dct = {'data': 5, 'science': 3, 'machine':1, 'learning': 8}
a={}
for i in l:
    if i in dct:
        a[i]=dct[i]
    else:
        a[i]=len(i)
print(a)    
