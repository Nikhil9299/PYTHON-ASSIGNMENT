
f=open("p12.txt", 'r')
c = f.read()
p=c.splitlines()

s=p[::-1]


f=open("p12.txt", 'w')
c=f.write('\n'.join(s))

print("File content has been reversed and written back to the file.")
