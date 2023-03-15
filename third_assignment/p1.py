
n=[10, 5, 20, 30, 15, 25]
a=n[0]
b=n[1]
for i in range(2,len(n)):
    # If the current element is greater than a, update both a and b
    if n[i]>a:
        b=a
        a=n[i]
    # If the current element is between a and b, update only b
    elif n[i]>b:
        b=n[i]
print(b)