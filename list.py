


a=["hello","ok"]
b=["sir","take"]
c=[]
i=0
while i<len(a):
    j=0
    while j<len(a):
        c.append(a[i]+b[j])
        j=j+1
    i=i+1
print(c)
    