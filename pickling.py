import pickle
a=["nikhil","python"]
#pickling
with open("pickling.txt","wb") as f:
    pickle.dump(a,f)
#unpickling    
w=open("pickling.txt","rb")
s=pickle.load(w)
print(s)