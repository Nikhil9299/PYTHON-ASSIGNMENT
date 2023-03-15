a=int(input())
b=int(input())
try:
    print(a/b)
except:
    print("Hey you can not divide a number by zero")
finally:
    print("****")        