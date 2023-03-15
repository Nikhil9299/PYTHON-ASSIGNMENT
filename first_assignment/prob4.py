test_list=[2323,82,129388,95]
a={}
for i in test_list:
    s=str(i)
    half_s=len(s)//2
    key=int(s[:half_s])
    val=int(s[half_s:])
    a[key]=val
print(a)    