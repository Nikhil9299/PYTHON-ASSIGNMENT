import pickle
dct = {111: "Eric", 112: "Kyle", 113: "Butters"}
#pickling
with open('test.txt','wb') as a:
    pickle.dump(dct,a)

#unpickling
with open('test.txt','rb') as a:
    dct2=pickle.load(a)
print(dct2[112])    