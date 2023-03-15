n=int(input())
for i in range(1,n+1):
    if i==1:
        print(" "*(n-i)+"*")
    else:
        space=" "*(n-i)
        star="*"
        dash="-"*(i-1)
        print(space+star+dash+star)    
        
    