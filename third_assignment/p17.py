def Winner(*teams):
    a=[]
    for i in teams:
        a.append(i[0]*3 + i[1]*1 + i[2]*(-1))
    s=max(a)  
    index = a.index(s)
    return ("Winner: Team{}").format(index+1)
    
Team1=(3, 4, 2)
Team2=(5, 0, 2)
Team3=(0, 0, 1) 

f=Winner(Team1,Team2,Team3)
print(f)
