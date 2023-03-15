def reverse_vowel(a):
    s=[]
    d=''
    vowels=('aeiouAEIOU')
    for i in a:
        if i in vowels:
            s.append(i)
    #print(s)        
    for i in a:
        if i in vowels:
            d+=s.pop()
        else:
            d+=i          
    return d          


a="Hello"
o=reverse_vowel(a)
print(o)



