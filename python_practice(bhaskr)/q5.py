a={'Msys Technologies':'Sanjay Sehgal', 'Infosys':'Salil Parekh',
'TCS':'Rajesh Gopinathan', 'Wipro':'Thierry Delaporte'} 
key={}
s=list(sorted(a))
print(s)
for i in s:
    key[i] = a[i]
print(key)