a={'India':'New Delhi', 'USA':'Washington D.C.', 'Nepal':'Kathmandu'} 
l=a.keys()
list_keys=[]
for i in l:
    list_keys.append(i)
print(list_keys)   

s=a.values()
list_values=[]
for i in s:
    list_values.append(i)
print(list_values)   
key="Australia"
if key in a:
    print(a[key])
else:
    print("NA")

