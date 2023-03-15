def anagram(s1,s2):
    if sorted(s1.lower()) == sorted(s1.lower()) :
        return True
    else:
        return False
s1=input()
s2=input()
s=anagram(s1,s2)
print(s)