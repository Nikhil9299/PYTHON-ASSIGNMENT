def is_strong(password):
    sp=('!@#$%^&*()_-+=[]{}:;?/.,><"')
    u,l,d,s=0,0,0,0
    if len(password)>=8:
        for i in password:
            if i.isdigit():
                d+=1
            elif i.isupper():
                u+=1
            elif i.islower():
                l+=1
            elif i in sp:
                s+=1
    if (u>=1 and l>=1 and d>=1 and s>=1 and (u+l+d+s)==len(password)):
        f=True
    else:
        f=False
    return f    
    
password=input()        
h=is_strong(password)
print(h)