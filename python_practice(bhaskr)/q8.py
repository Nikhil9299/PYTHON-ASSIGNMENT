a=input()
s=int(a)
if 0<=s<=100:
    if s>=91 and s<=100:
        print("A1")
    elif s>=81 and s<=90:
        print("A2")
    elif s>=71 and s<=80:
        print("B1")
    elif s>=61 and s<=70:
        print("B2")
    elif s>=51 and s<=60:
        print("C1")
    elif s>=40 and s<=50:
        print("C2")
    elif s< 40:
        print("Fail")  
else:
    print("Invalid marks")